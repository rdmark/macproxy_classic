# Edit this file to configure Macproxy Classic settings

# Used by weather extension (which currently only works for United States)
# ZIP_CODE = "YOUR_ZIP_CODE"

# Commented-out extensions require additional preparation steps before they can be used.
ENABLED_EXTENSIONS = [
	"hackaday",
	#"notyoutube",
	"npr",
	"reddit",
	"waybackmachine",
	#"weather",
	"wiby",
	"wikipedia",
]

# While SIMPLIFY_HTML is True, you can use WHITELISTED_DOMAINS to disable post-processing for
# specific sites (only perform HTTPS -> HTTP conversion and character conversion (if CONVERT_CHARACTERS is True),
# without otherwise modifying the page's source code).
WHITELISTED_DOMAINS = [
	#"example.com",
]

# Optionally, load a preset (.py file) from /presets, optimized for compatibility
# with a specific web browser. Enabling a preset may override one or more of the
# settings that follow below.
# The default values target compatability with the MacWeb 2.0 browser.
#PRESET = "wii_internet_channel"

# --------------------------------------------------------------------------------------
# *** One or more of the following settings may be overridden if you enable a preset ***
# --------------------------------------------------------------------------------------

# If True, parse HTML responses to strip specified tags and attributes.
# If False, always return the full, unmodified HTML as served by the requested site or extension
# (only perform HTTPS -> HTTP conversion and character conversion (if CONVERT_CHARACTERS is True),
# without otherwise modifying the page's source code).
SIMPLIFY_HTML = True

# If SIMPLIFY_HTML is True, unwrap these HTML tags during processing:
TAGS_TO_UNWRAP = [
	"noscript",
]

# If SIMPLIFY_HTML is True, strip these HTML tags during processing:
TAGS_TO_STRIP = [
	"script",
	"link",
	"style",
	"source",
]

# If SIMPLIFY_HTML is True, strip these HTML attributes during processing:
ATTRIBUTES_TO_STRIP = [
	"style",
	"onclick",
	"class",
	"bgcolor",
	"text",
	"link",
	"vlink"
]

# Process images for optimal rendering on your device/browser:
CAN_RENDER_INLINE_IMAGES = False # Mostly used to conditionally enable landing page images (ex: waybackmachine.py)
RESIZE_IMAGES = True
MAX_IMAGE_WIDTH = 512 # Only used if RESIZE_IMAGES is True
MAX_IMAGE_HEIGHT = 342 # Only used if RESIZE_IMAGES is True
CONVERT_IMAGES = True
CONVERT_IMAGES_TO_FILETYPE = "jpg" # Only used if CONVERT_IMAGES is True
DITHERING_ALGORITHM = "FLOYDSTEINBERG" # Only used if CONVERT_IMAGES is True and CONVERT_IMAGES_TO_FILETYPE == "gif"

# Conditionally enable/disable use of CONVERSION_TABLE
CONVERT_CHARACTERS = True

# Convert text characters for compatability with specific browsers
CONVERSION_TABLE = {
	"¢": b"cent",
	"&cent;": b"cent",
	"€": b"EUR",
	"&euro;": b"EUR",
	"&yen;": b"YEN",
	"&pound;": b"GBP",
	"«": b"'",
	"&laquo;": b"'",
	"»": b"'",
	"&raquo;": b"'",
	"‘": b"'",
	"&lsquo;": b"'",
	"’": b"'",
	"&rsquo;": b"'",
	"“": b"''",
	"&ldquo;": b"''",
	"”": b"''",
	"&rdquo;": b"''",
	"–": b"-",
	"&ndash;": b"-",
	"—": b"--",
	"&mdash;": b"--",
	"―": b"-",
	"&horbar;": b"-",
	"·": b"-",
	"&middot;": b"-",
	"‚": b",",
	"&sbquo;": b",",
	"„": b",,",
	"&bdquo;": b",,",
	"†": b"*",
	"&dagger;": b"*",
	"‡": b"**",
	"&Dagger;": b"**",
	"•": b"-",
	"&bull;": b"*",
	"…": b"...",
	"&hellip;": b"...",
	"\u00A0": b" ",
	"&nbsp;": b" ",
	"±": b"+/-",
	"&plusmn;": b"+/-",
	"≈": b"~",
	"&asymp;": b"~",
	"≠": b"!=",
	"&ne;": b"!=",
	"&times;": b"x",
	"⁄": b"/",
	"°": b"*",
	"&deg;": b"*",
	"′": b"'",
	"&prime;": b"'",
	"″": b"''",
	"&Prime;": b"''",
	"™": b"(tm)",
	"&trade;": b"(TM)",
	"&reg;": b"(R)",
	"®": b"(R)",
	"&copy;": b"(c)",
	"©": b"(c)",
	"é": b"e",
	"ø": b"o",
	"Å": b"A",
	"â": b"a",
	"Æ": b"AE",
	"æ": b"ae",
	"á": b"a",
	"ō": b"o",
	"ó": b"o",
	"ū": b"u",
	"⟨": b"<",
	"⟩": b">",
	"←": b"<",
	"›": b">",
	"‹": b"<",
	"&larr;": b"<",
	"→": b">",
	"&rarr;": b">",
	"↑": b"^",
	"&uarr;": b"^",
	"↓": b"v",
	"&darr;": b"v",
	"↖": b"\\",
	"&nwarr;": b"\\",
	"↗": b"/",
	"&nearr;": b"/",
	"↘": b"\\",
	"&searr;": b"\\",
	"↙": b"/",
	"&swarr;": b"/",
	"─": b"-",
	"&boxh;": b"-",
	"│": b"|",
	"&boxv;": b"|",
	"┌": b"+",
	"&boxdr;": b"+",
	"┐": b"+",
	"&boxdl;": b"+",
	"└": b"+",
	"&boxur;": b"+",
	"┘": b"+",
	"&boxul;": b"+",
	"├": b"+",
	"&boxvr;": b"+",
	"┤": b"+",
	"&boxvl;": b"+",
	"┬": b"+",
	"&boxhd;": b"+",
	"┴": b"+",
	"&boxhu;": b"+",
	"┼": b"+",
	"&boxvh;": b"+",
	"█": b"#",
	"&block;": b"#",
	"▌": b"|",
	"&lhblk;": b"|",
	"▐": b"|",
	"&rhblk;": b"|",
	"▀": b"-",
	"&uhblk;": b"-",
	"▄": b"_",
	"&lhblk;": b"_",
	"▾": b"v",
	"&dtrif;": b"v",
	"&#x25BE;": b"v",
	"&#9662;": b"v",
	"♫": b"",
	"&spades;": b"",
	"\u200B": b"",
	"&ZeroWidthSpace;": b"",
	"\u200C": b"",
	"\u200D": b"",
	"\uFEFF": b"",
}