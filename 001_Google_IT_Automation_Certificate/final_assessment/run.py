#!/usr/bin/env python3

import os, requests, json

def upload_fruit_description(url, description_directory):
    fruit = {}
    for file in os.listdir(description_directory):
        fruit.clear()
        filename = os.path.join(description_directory, file)
        with open(filename) as opened_file:
            lines = opened_file.readlines()
            description = ""
            for i in range(2, len(lines)):
                description += lines[i].strip('\n').replace(u'\xa0', u'')
            fruit["description"] = description
            fruit["weight"] = int(lines[1].strip('\n').strip('lbs'))
            fruit["name"] = lines[0].strip('\n')
            fruit["image_name"] = "{}.jpeg".format(item.strip('.txt'))
            print(fruit)
            if url != "":
                response = requests.post(url, json=fruit)
                print(response.request.url)
                print(response.status_code)
    return 0

if __name__ == '__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    upload_fruit_description(url, description_directory)
