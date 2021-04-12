#!/usr/bin/env python3

import os
import requests

def transform_feedback(file_path):
    output = {}

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            line_index = 0
            for line in file.readlines():
                key = 'title'
                if line_index == 1:
                    key = 'name'
                elif line_index == 2:
                    key = 'date'
                elif line_index == 3:
                    key = 'feedback'

                output[key] = line.replace("\n", "")
                line_index = line_index + 1
        file.close()

    return output

def send_feedback_to_web_service(feedback):
    response = requests.post("http://<external-ip>/feedback/", json=feedback)
    response.raise_for_status()

def main():
    for root, directories, files in os.walk("data/feedback/"):
        for filename in files:
            if filename.endswith(".txt"):
                feedback = transform_feedback(os.path.join(root, filename))
                send_feedback_to_web_service(feedback)

main()
