#!/usr/bin/env python3

import os, sys
from PIL import Image

user = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images/'.format(user)
for image_name in os.listdir(image_directory):
    if not image_name.startswith('.') and 'tiff' in image_name:
        image_path = os.path.join(image_directory, image_name)
        path = os.path.splitext(image_path)[0]
        image = Image.open(image_path)
        new_path = '{}.jpeg'.format(path)
        image.convert('RGB').resize((600, 400)).save(new_path, "JPEG")
