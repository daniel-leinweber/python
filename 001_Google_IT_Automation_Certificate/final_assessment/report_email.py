#!/usr/bin/env python3

import datetime, os

from run import upload_fruit_description
from reports import generate_report
from emails import generate_email, send_email

def generate_pdf_body(input_for, description_directory):
    res = []
    wt = []
    for file in os.listdir(description_directory):
        filename = os.path.join(description_directory, file)
        with open(filename) as opened_file:
            lines = opened_file.readlines()
            name = lines[0].strip('\n')
            weight = lines[1].strip('\n')
            print(name, weight)
            res.append('name: {}'.format(name))
            wt.append('weight: {}'.format(weight))
            print(res)
            print(wt)

    new_obj = ""
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_obj += '{}<br />{}<br /><br />'.format(res[i], wt[i])

    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on {}'.format(current_date)
    generate_report('/tmp/processed.pdf', title, generate_pdf_body('pdf', description_directory))
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    msg = generate_email("automation@example.com", "{}@example.com".format(user), email_subject, email_body, "/tmp/processed.pdf")
    send_email(msg)
