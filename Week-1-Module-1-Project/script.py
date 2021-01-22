#!/usr/bin/env python3

from PIL import Image
import os
import sys

# List all files in a directory using os.listdir
user=os.getenv('USER')
basepath = "/home/{}/images/".format(user)
pictureFiles = []
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        pictureFiles.append(entry)

for entry in pictureFiles:
    print(entry)

for picture in pictureFiles:
    if picture == ".DS_Store":
        continue
    else:
        im = Image.open(basepath + picture)
        im.convert('RGB').rotate(-90).resize((128,128)).save("/opt/icons/" + picture, "JPEG")
