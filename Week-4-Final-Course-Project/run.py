#!/usr/bin/env python3

import os
import requests

# number used to sync adding the image into the dictionary
number = 0

# List all files in a directory using os.listdir
descriptionpath = "supplier-data/descriptions/"
basepath = "supplier-data/images/"

pictureFiles = []
for image in os.listdir(basepath):
    if '.jpeg' in image:
        pictureFiles.append(image)
sort_picture_files = sorted(pictureFiles)

descriptionFiles = sorted(os.listdir(descriptionpath))

for entry in descriptionFiles:
    descriptionDict = {}
    # open file and read in details
    with open(descriptionpath + entry) as textfile:
        count = 0
        # breaking up textfile line by line to sort the information into dictionary
        for line in textfile:
            if count == 0:
                descriptionDict['name'] = line
            elif count == 1:
                weight = line[:-4]
                descriptionDict['weight'] = str(weight)
            elif count == 2:
                descriptionDict['description'] = line
            count += 1
    
    # adding image to dictionary
    descriptionDict['image_name'] = sort_picture_files[number]
    number += 1

    # replace XXXXX with ipaddress of site
    ipaddress = "XXXXX"

    # use request POST module to upload dictionary content to site
    response = requests.post("http://" + ipaddress + "/fruits/", json = descriptionDict)

    # check status of response
    print("Status: " + str(response.status_code))
    textfile.close()

