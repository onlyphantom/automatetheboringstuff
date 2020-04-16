"""Resize if necessary and add logo

Reduce width or height (whichever is larger) of all images in a specified 
directory to 300 pixels and scale it proportionally

Paste a logo onto the image and save into a separate directory
"""
import os
from PIL import Image

FIT_SIZE = 300
LOGO_NAME = 'corgi.png'
LOGO_PATH = os.path.join('assets', LOGO_NAME)
OUTPUT_DIR_NAME = 'withLogo'

logo = Image.open(LOGO_PATH)
logo = logo.resize((int(logo.size[0] * 0.2), int(logo.size[1] * 0.2)))
logo_w, logo_h = logo.size

os.makedirs(OUTPUT_DIR_NAME, exist_ok=True)
for f in os.listdir('assets'):
    _, ext = os.path.splitext(f)
    if ext.lower() in ['.png', '.jpg'] and f != LOGO_NAME:
        filename = os.path.join('assets', f)
        im = Image.open(filename)
        w, h = im.size

        if w > FIT_SIZE or h > FIT_SIZE:
            if w > h:
                h = int((FIT_SIZE / w) * h)
                w = FIT_SIZE
            else:
                w = int((FIT_SIZE / h) * w)
                h = FIT_SIZE
            print(f'Resizing {filename} to {w}x{h}')
            im = im.resize((w, h))
        
        print(f'Adding logo to {filename}')
        im.paste(logo, (w - logo_w - 10, h - logo_h - 10), logo)
        im.save(os.path.join(OUTPUT_DIR_NAME, f))
