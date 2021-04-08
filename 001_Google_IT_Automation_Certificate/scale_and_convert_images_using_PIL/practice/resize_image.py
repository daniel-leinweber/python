#!/usr/bin/env python3

from PIL import Image

image = Image.open("image.jpg")
new_image = image.resize((640, 480))
new_image.save("resized_image.jpg")
