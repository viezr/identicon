'''
Icon image generator from string hash.
'''
import io
import hashlib
from PIL import Image, ImageDraw
from random import choice


def create_image(value = None, size = None) -> bytes:
    '''
    Return bytes of png image, generated from string hash.
    '''
    value, size = _parse_input(value, size)
    color = choice(["#a87633", "#7ff95d", "#89ba38", "#45a1fb",
        "#d67b6a", "#931216", "#8c1aac"])

    pixmap = _create_pixmap(value)
    out_img = Image.new("RGB", (5, 5), (255, 255, 255))
    draw = ImageDraw.Draw(out_img)
    draw.point(pixmap, fill=color)
    im_resized = out_img.resize((size, size), resample=Image.BOX)

    img_bytes = io.BytesIO()
    im_resized.save(img_bytes, format='PNG')
    img_bytes_out = img_bytes.getvalue()
    return img_bytes_out

def _parse_input(value, size) -> tuple:
    value = "abc" if not isinstance(value, str) else value
    if isinstance(size, str) and size.isdecimal():
        size = int(size)
    if not isinstance(size, int) or size not in range(5, 256):
        size = 80
    return (value, size)

def _create_pixmap(value: str) -> list:
    '''
    Create list of tuples (x,y) for drawing image.
    '''
    table = _create_table(value)
    pixmap = []
    for y, row in enumerate(table):
        pixmap += [(x, y) for x, col in enumerate(row) if col == 1]
    return pixmap

def _create_table(value: str) -> list:
    '''
    Create bits table 5x5 from hash of string.
    '''
    bin_str_value = _hash_func(value.encode())[2:]
    table = []
    k = 1 if len(value) < 6 else 3
    for idx, letter in enumerate(bin_str_value):
        if idx > 4:
            break
        col1 = int(bin_str_value[idx])
        col2 = int(bin_str_value[idx + 5*k])
        col3 = int(bin_str_value[idx + 10*k])
        col1 = 1 if all(x == 0 for x in (col1, col2, col3)) else col1
        row = (col3, col2, col1, col2, col3)
        table.append(row)
    return table

def _hash_func(value: str) -> str:
    hash_value = hashlib.md5(value)
    int_value = int.from_bytes(hash_value.digest(), "big")
    bin_str_value = bin(int_value)
    return bin_str_value
