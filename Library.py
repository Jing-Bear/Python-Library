from PIL import Image
from io import BytesIO

# Constants
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


def get_rgba(data):
    img = Image.open(BytesIO(data))
    pic = img.load()
    width, height = img.size
    pixels = []
    for i in range(height):
        for j in range(width):
            pixels.append(pic[j, i])
    return pixels


def rot(encoded, n=13):
    out = ""
    for c in encoded:
        if c.isalpha():
            if c.isupper():
                out = out + UPPER[(UPPER.find(c) + n) % 26]
            else:
                out = out + LOWER[(LOWER.find(c) + n) % 26]
        else:
            out = out + c
    return out

