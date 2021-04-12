#!/usr/bin/env python3

import requests, os

url = "http://localhost/upload/"
user = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images/'.format(user)
files = os.listdir(image_directory)

for image_name in files:
    if not image_name.startswith('.') and 'jpeg' in image_name:
        image_path = os.path.join(image_directory, image_name)
        with open(image_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
