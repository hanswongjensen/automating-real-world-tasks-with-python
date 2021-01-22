#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
basepath = "supplier-data/images/"

pictureFiles = []
for image in os.listdir(basepath):
    if '.jpeg' in image:
        pictureFiles.append(image)

for image in pictureFiles:
    with open(basepath + image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
