#! /usr/bin/env python3
# coding = utf-8

# resizeAndAddLogo.py - Resize all images in current working directory to fit

import os
import sys
from PIL import Image
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir)))
from utils import resourcesLoader

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = resourcesLoader.getRealPath('catlogo.png')

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('out/withLogo', exist_ok=True)
baseDir = resourcesLoader.ResourceDirPath
for filename in [os.path.join(baseDir, f) for f in os.listdir(baseDir)]:
    if not (filename.endswith('.png')) or filename.endswith('.jpg') \
            or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size
    print(width, height)
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image.
        print('Resizing %s...' % filename)
        im = im.resize((width, height))
    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('out/withLogo', os.path.split(filename)[1]))
