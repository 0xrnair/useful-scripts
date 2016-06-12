#!/usr/bin/env python
'''
A simple script to find when Image was created/uploaded in imgur

'''
from lxml import html
import requests,sys

find_attribute = 'create_datetime'
if len(sys.argv) < 2:
	print "[*] Usage : ./imgur.py http://<imgur-url>"
	sys.exit(-1)

img_url = sys.argv[1]
page = requests.get(img_url)
data = page.content
p = data.find(find_attribute) + 18
print "Created Date (GMT) of Image: "+data[p:p+19]
