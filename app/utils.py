from io import BytesIO

from flask import send_file
from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)


def generate_image(caller_id):
    img = Image.open("assets/base.png")
    font = ImageFont.truetype("assets/arial-black.ttf", font_size(caller_id))
    text = Image.new('L', (428, 349))
    draw = ImageDraw.Draw(text)
    draw.text((10, 105), caller_id, font=font, fill=255)
    img_to_paste = text.rotate(-10, expand=1)
    img.paste("#FFF", (0, 0), img_to_paste)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', cache_timeout=0)


def font_size(caller_id):
    caller_id_num_chars = len(caller_id)
    if caller_id_num_chars < 7:
        size = 32
    elif caller_id_num_chars > 10:
        size = 18
    else:
        size = 24
    return size
