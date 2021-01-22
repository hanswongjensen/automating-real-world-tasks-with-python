#!/usr/bin/env python3

import os
import reports
from datetime import date
import emails

# List all files in a directory using os.listdir
descriptionpath = "supplier-data/descriptions/"

# Make a list of required names and weights for report generation
fruit_info = []

# Create dictionary of name and weight from individual files
for entry in os.listdir(descriptionpath):
    descriptionDict = {}
    #open file and read in details
    with open(descriptionpath + entry) as textfile:
        count = 0
        #breaking up textfile line by line to sort the information into dictionary
        for line in textfile:
            if count == 0:
                descriptionDict['name'] = line
            elif count == 1:
                descriptionDict['weight'] = line
            else:
                fruit_info.append("name: " + descriptionDict['name'] + "\n weight: " + descriptionDict['weight'] + "\n")
            count += 1


# Generate report
date_today = date.today().strftime(“%B %d, %Y”)
information = "<br/><br/>".join(fruit_info)
reports.generate("/tmp/processed.pdf", "Processed Update on " + date_today,  information)

#Send email
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachment_path = "/tmp/processed.pdf"

final_email = emails.generate(sender, recipient, subject, body, attachment_path)
emails.send(final_email)
