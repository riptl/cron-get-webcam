#!/usr/bin/env python3
#
# https://github.com/terorie/cron-get-webcam

import calendar
import email.utils
import mimetypes
import os.path
import requests
import shutil
import sys
import time

mimetypes.init()

if len(sys.argv) != 3:
	sys.exit("Usage ./cron-webcam-pic.py <dir> <url>")

prefix = sys.argv[1]
url    = sys.argv[2]

# Request picture
r = requests.get(url, stream=True)
last_modified = r.headers['last-modified']
content_type  = r.headers['content-type']
timestamp = email.utils.parsedate(last_modified)
extension = mimetypes.guess_extension(content_type)

# Generate file path
t = timestamp
day = '%d-%02d-%02d' % (t[0], t[1], t[2])
clock = '%02d%02d%02d' % (t[3], t[4], t[5]) + extension
dirs = os.path.join(prefix, day)
fullpath = os.path.join(dirs, clock)

# Check if file exists
if os.path.exists(fullpath):
	sys.exit(0)

# Download new file
os.makedirs(dirs, exist_ok=True)
with open(fullpath, 'wb') as f:
	shutil.copyfileobj(r.raw, f)

# Set modification time
unix = calendar.timegm(timestamp)
os.utime(fullpath, (unix, unix))
