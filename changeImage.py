#!/usr/bin/env python3

from PIL import Image
import os
import sys

# List all files in a directory using os.listdir
basepath = "supplier-data/images/"
pictureFiles = []
for entry in os.listdir(basepath):
    if entry == "README":
        continue
    elif entry == "LICENSE":
        continue
    elif os.path.isfile(os.path.join(basepath, entry)):
        pictureFiles.append(entry)

# Check images
#for image in pictureFiles:
    #print(image)

for picture in pictureFiles:
    if picture == ".DS_Store":
        continue
    else:
        im = Image.open(basepath + picture)
        im.convert('RGB').resize((600,400)).save(basepath + picture[:-5] + ".jpeg", "JPEG")
