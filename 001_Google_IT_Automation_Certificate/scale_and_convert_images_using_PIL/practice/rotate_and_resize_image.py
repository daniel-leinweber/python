#!/usr/bin/env python3

from PIL import Image

image = Image.open("image.jpg")
image.rotate(180).resize((640, 480)).save("rotated_and_resized_image.jpg")
