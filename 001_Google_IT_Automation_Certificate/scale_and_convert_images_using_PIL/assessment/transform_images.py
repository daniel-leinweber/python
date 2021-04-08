#!/usr/bin/env python3

import os
import sys
from PIL import Image

def transform_image(source_image_path, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)

    if os.path.exists(source_image_path):
        filename = os.path.splitext(os.path.basename(source_image_path))[0]
        target_name = "{}{}".format(destination_folder, filename)
        image = Image.open(source_image_path)
        image.convert("RGB").rotate(-90).resize((128, 128)).save(target_name, "JPEG", quality=95)

def main():
    source_folder = "images/"
    destination_folder = "dest/"
    for root, directories, files in os.walk(source_folder):
        for filename in files:
            source_image_path = "{}{}".format(root, filename)
            transform_image(source_image_path, destination_folder)

main()
