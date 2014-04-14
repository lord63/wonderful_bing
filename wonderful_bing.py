#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
import os
import time
import requests


def DownloadAndSet(imgUrl):
    filename = imgUrl.split('/')[-1]
    local_filename = changename(filename) + ".jpg"
    if os.path.isfile("/home/lord63/pictures/bing/"+local_filename):
    	return  # if the picture had been downloaded, stop doing the following things
    r = requests.get(imgUrl, stream=True)  # to get the raw content
    with open("/home/lord63/picture/bing/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
    print "Download Image File=", local_filename
    setWallpaper("/home/lord63/picture/bing/"+local_filename)

# make the picture name look nicer
def changename(filename):
	p = re.compile('([^_])*')
	m = p.search(filename)
	return m.group()

def setWallpaper(picPath):
    os.system('hsetroot  -extend '+ picPath)


time.sleep(5)
r = requests.get('http://cn.bing.com')

# using regular expression to get the picture url
p = re.compile('http://s.cn.bing.net/az/hprichbg/rb/([^\']+)')
m = p.search(r.content)
Url = m.group()

DownloadAndSet(Url)



