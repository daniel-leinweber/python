#!/usr/bin/env python3

from PIL import Image

image = Image.open("image.jpg")
new_image = image.rotate(90)
new_image.save("rotated_image.jpg")
