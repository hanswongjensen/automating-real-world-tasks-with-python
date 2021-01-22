#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

# Check CPU usage
usage = psutil.cpu_percent(1)

# Check Disk usage
disk_usage = shutil.disk_usage("/")
free_space = disk_usage.free / disk_usage.total *100

# Check Available memory
available_memory = psutil.virtual_memory().available / (1024*1024)

# Check localhost
localhost = socket.gethostbyname('localhost')

# Do the checks
error = False

if usage > 80:
    message = "CPU usage is over 80%"
    error = True
if free_space < 20:
    message = "Available disk space is less than 20%"
    error = True
if available_memory < 500:
    message = "Available memory is less than 500MB"
    error = True
if localhost != '127.0.0.1':
    message = "localhost cannot be resolved to 127.0.0.1"
    error = True

if error is True:
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Error - " + message
    body = "Please check your system and resolve the issue as soon as possible."
    email = emails.generate_no_attachment(sender, recipient, subject, body)
    emails.send(email)
