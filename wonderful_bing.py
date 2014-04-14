#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import os
import time

import requests


def download_and_set(imgUrl):  
    filename = imgUrl.split('/')[-1] 
    local_filename = change_name(filename) + ".jpg"
    if os.path.isfile("/home/lord63/pictures/bing/"+local_filename):
    	return  # if the picture had been downloaded, stop doing the following things
    r = requests.get(imgUrl, stream=True)  # to get the raw content 
    with open("/home/lord63/picture/bing/"+local_filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):        
            f.write(chunk)  
    print "Download Image File=", local_filename     
    set_wallpaper("/home/lord63/picture/bing/"+local_filename)

# make the picture name look nicer
def change_name(filename):
	p = re.compile('([^_])*')
	m = p.search(filename)
	return m.group()

def set_wallpaper(picPath):
    os.system('gsettings set org.gnome.desktop.background picture-uri file://' + picPath)

#------------------------------------------------------------#
time.sleep(5)

r = requests.get('http://cn.bing.com')

# using regular expression to get the picture url
p = re.compile('http://s.cn.bing.net/az/hprichbg/rb/([^\']+)')
m = p.search(r.content)
Url = m.group()

download_and_set(Url)



   