import os
import io
import hashlib
import requests
from PIL import Image, UnidentifiedImageError
import mimetypes
from utils.debug_utils import debug_print

CACHE_DIR = os.path.join(os.path.dirname(__file__), "cached_images")
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"

def is_image_url(url):
	mime_type, _ = mimetypes.guess_type(url)
	return mime_type and mime_type.startswith('image/')

def optimize_image(image_data, resize=True, max_width=512, max_height=342, 
				  convert=True, convert_to='gif', dithering='FLOYDSTEINBERG'):
	try:
		img = Image.open(io.BytesIO(image_data))
	except UnidentifiedImageError:
		print("Error: Provided data is not a valid image.")
		return image_data
	except Exception as e:
		print(f"Error opening image: {str(e)}")
		return image_data

	# Convert RGBA images to RGB with white background
	if img.mode == 'RGBA':
		background = Image.new('RGB', img.size, (255, 255, 255))
		background.paste(img, mask=img.split()[3])
		img = background
	elif img.mode != 'RGB':
		img = img.convert('RGB')

	# Resize if enabled and necessary
	if resize and max_width and max_height:
		width, height = img.size
		if width > max_width or height > max_height:
			ratio = min(max_width / width, max_height / height)
			new_size = (int(width * ratio), int(height * ratio))
			img = img.resize(new_size, Image.Resampling.LANCZOS)

	# Convert format if enabled
	if convert and convert_to:
		if convert_to.lower() == 'gif':
			# For black and white GIF
			img = img.convert("L")  # Convert to grayscale first
			dither_method = Image.Dither.FLOYDSTEINBERG if dithering and dithering.upper() == 'FLOYDSTEINBERG' else None
			img = img.convert("1", dither=dither_method)
		else:
			# For other format conversions
			img = img.convert(img.mode)

	output = io.BytesIO()
	# Map common extensions to Pillow format names
	format_map = {
		'jpg': 'JPEG',
		'jpeg': 'JPEG',
		'png': 'PNG',
		'gif': 'GIF',
		'webp': 'WEBP'
	}
	save_format = convert_to.lower() if convert and convert_to else (img.format or 'PNG')
	save_format = format_map.get(save_format, save_format.upper())

	try:
		img.save(output, format=save_format, optimize=True)
	except Exception as e:
		print(f"Error saving image (format={save_format}): {str(e)}")
		return image_data

	return output.getvalue()

def fetch_and_cache_image(url, content=None, resize=True, max_width=512, max_height=342,
						 convert=True, convert_to='gif', dithering='FLOYDSTEINBERG'):
	try:
		debug_print(f"Processing image: {url}")

		# Generate filename with appropriate extension
		extension = convert_to.lower() if convert and convert_to else "gif"
		file_name = hashlib.md5(url.encode()).hexdigest() + f".{extension}"
		file_path = os.path.join(CACHE_DIR, file_name)

		if not os.path.exists(file_path):
			debug_print(f"Optimizing and caching image: {url}")
			if content is None:
				try:
					response = requests.get(url, stream=True, headers={"User-Agent": USER_AGENT})
					response.raise_for_status()
					content = response.content
				except requests.RequestException as e:
					print(f"Error downloading image: {url}, Error: {str(e)}")
					return None

			# Only process if image conversion or resizing is enabled
			if convert or resize:
				try:
					optimized_image = optimize_image(
						content,
						resize=resize,
						max_width=max_width,
						max_height=max_height,
						convert=convert,
						convert_to=convert_to,
						dithering=dithering
					)
				except Exception as e:
					print(f"Error optimizing image: {url}, Error: {str(e)}")
					return None
			else:
				optimized_image = content

			try:
				with open(file_path, 'wb') as f:
					f.write(optimized_image)
			except OSError as e:
				print(f"Error saving image to cache: {file_path}, Error: {str(e)}")
				return None
		else:
			debug_print(f"Image already cached: {url}")

		cached_url = f"/cached_image/{file_name}"
		debug_print(f"Cached URL: {cached_url}")
		return cached_url

	except Exception as e:
		print(f"Error processing image: {url}, Error: {str(e)}")
		return None

# Ensure cache directory exists
if not os.path.exists(CACHE_DIR):
	os.makedirs(CACHE_DIR)
