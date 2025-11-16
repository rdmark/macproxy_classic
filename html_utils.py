"""
HTML transcoding helper methods for Macproxy
"""

from bs4 import BeautifulSoup
import re

CONVERSION_TABLE = {
    # Currency symbols
    "¢": b"cent",
    "&cent;": b"cent",
    "€": b"EUR",
    "&euro;": b"EUR",

    # Quotes and dashes
    "«": b"'",
    "&laquo;": b"'",
    "»": b"'",
    "&raquo;": b"'",
    "‘": b"'",
    "&lsquo;": b"'",
    "’": b"'",
    "&rsquo;": b"'",
    "“": b"''",  # Left double quote
    "&ldquo;": b"''",
    "”": b"''",  # Right double quote
    "&rdquo;": b"''",
    "–": b"-",   # En dash
    "&ndash;": b"-",
    "—": b"--",  # Em dash
    "&mdash;": b"--",
    "―": b"-",   # Horizontal bar
    "&horbar;": b"-",

    # Punctuation and special characters
    "·": b"-",   # Middle dot
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
    "&hellip;": b".",
    "\u00A0": b" ",
    "&nbsp;": b" ",

    # Math symbols
    "±": b"+/-",
    "&plusmn;": b"+/-",
    "≈": b"~",
    "&asymp;": b"~",
    "≠": b"!=",
    "&ne;": b"!=",
    "&times;": b"x",
    "⁄": b"/",

    # Miscellaneous symbols
    "°": b"*",
    "&deg;": b"*",
    "′": b"'",
    "&prime;": b"'",
    "″": b"''",
    "&Prime;": b"''",
    "™": b"(tm)",
    "&trade;": b"(TM)",
    "®": b"(R)",
    "&reg;": b"(R)",
    "©": b"(c)",
    "&copy;": b"(c)",
    "⟨": b"<",
    "⟩": b">",

    # Arrows
    "←": b"<",   # Left arrow
    "&larr;": b"<",
    "→": b">",   # Right arrow
    "&rarr;": b">",
    "↑": b"^",    # Up arrow
    "&uarr;": b"^",
    "↓": b"v",    # Down arrow
    "&darr;": b"v",
    "↖": b"\\",   # Diagonal arrows
    "&nwarr;": b"\\",
    "↗": b"/",    # Diagonal arrows
    "&nearr;": b"/",
    "↘": b"\\",   # Diagonal arrows
    "&searr;": b"\\",
    "↙": b"/",    # Diagonal arrows
    "&swarr;": b"/",

    # Box-drawing characters
    "─": b"-",  # Box drawings light horizontal
    "&boxh;": b"-",
    "│": b"|",  # Box drawings light vertical
    "&boxv;": b"|",
    "┌": b"+",  # Box drawings light down and right
    "&boxdr;": b"+",
    "┐": b"+",  # Box drawings light down and left
    "&boxdl;": b"+",
    "└": b"+",  # Box drawings light up and right
    "&boxur;": b"+",
    "┘": b"+",  # Box drawings light up and left
    "&boxul;": b"+",
    "├": b"+",  # Box drawings light vertical and right
    "&boxvr;": b"+",
    "┤": b"+",  # Box drawings light vertical and left
    "&boxvl;": b"+",
    "┬": b"+",  # Box drawings light down and horizontal
    "&boxhd;": b"+",
    "┴": b"+",  # Box drawings light up and horizontal
    "&boxhu;": b"+",
    "┼": b"+",  # Box drawings light vertical and horizontal
    "&boxvh;": b"+",


    # Block elements
    "█": b"#",  # Full block
    "&block;": b"#",
    "▌": b"|",  # Left half block
    "&lhblk;": b"|",
    "▐": b"|",  # Right half block
    "&rhblk;": b"|",
    "▀": b"-",  # Upper half block
    "&uhblk;": b"-",
    "▄": b"_",  # Lower half block
    "&lhblk;": b"_",

    # Downward triangle
    "▾": b"v",
    "&dtrif;": b"v",
    "&#x25BE;": b"v",  # Hexadecimal entity
    "&#9662;": b"v",  # Decimal entity

    # Musical note
    "♫": b"",
    "&spades;": b"",

    # Zero-width space
    "\u200B": b"",
    "&ZeroWidthSpace;": b"",
    "\u200C": b"",
    "\u200D": b"",
    "\uFEFF": b"",
}

def transcode_html(html, html_formatter, disable_char_conversion):
    """
    Uses BeautifulSoup to transcode payloads of the text/html content type
    """
    # Ensure html is in bytes
    if isinstance(html, str):
        html = html.decode("utf-8", errors="replace")

    if not disable_char_conversion:
        # Replace characters and entities based on the conversion table
        for key, replacement in CONVERSION_TABLE.items():
            html = html.replace(key.encode("utf-8"), replacement)

    soup = BeautifulSoup(html, "html.parser")

    # Remove all class attributes to make pages load faster
    for tag in soup.find_all(class_=True):
        del tag['class']

    for tag in soup(["script", "link", "style", "source", "picture"]):
        tag.decompose()
    for tag in soup():
        for attr in ["style", "onclick"]:
            if attr in tag.attrs:
                del tag[attr]
    for tag in soup(["base", "a"]):
        if "href" in tag.attrs:
            tag["href"] = tag["href"].replace("https://", "http://")
    for tag in soup("img"):
        if "src" in tag.attrs:
            tag["src"] = tag["src"].replace("https://", "http://")

    html = str(soup)
    html = html.replace('<br/>', '<br>')
    html = html.replace('<hr/>', '<hr>')

    # Ensure the output is properly encoded
    html_bytes = html.encode('utf-8')
    return html_bytes
