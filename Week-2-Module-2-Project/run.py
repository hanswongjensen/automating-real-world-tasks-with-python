#!/usr/bin/env python3

import os
import requests

# List all files in a directory using os.listdir
basepath = "/data/feedback/"
textDict = {}
for entry in os.listdir(basepath):
    #open file and read in details
    with open(basepath + entry) as textfile:
        count = 0
        #breaking up textfile line by line to sort the information into dictionary
        for line in textfile:
            if count == 0:
                textDict['title'] = line
            elif count == 1:
                textDict['name'] = line
            elif count == 2:
                textDict['date'] = line
            elif count == 3:
                textDict['feedback'] = line
            count += 1

    # Replace XXXXX with ipaddress of site
    ipaddress = "XXXXX"

    # Use request POST module to upload dictionary content to site
    response = requests.post("http://" + ipaddress + "/feedback/", json = textDict)

    # Check status of response
    print("Status: " + response.status_code)
    textfile.close()
