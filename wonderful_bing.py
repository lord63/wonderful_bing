# -*- coding=utf-8 -*-


import re
import requests


def DownloadImageFile(imgUrl):
    filename = imgUrl.split('/')[-1]
    local_filename = changename(filename) + ".jpg"
    print "Download Image File=", local_filename
    r = requests.get(imgUrl, stream=True)
    with open("/home/lord63/pictures/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
    return local_filename

# make the picture name look nicer
def changename(filename):
	p = re.compile('([^_])*')
	m = p.search(filename)
	return m.group()

r = requests.get('http://cn.bing.com')

# using regular expression to get the picture url
p = re.compile('http://s.cn.bing.net/az/hprichbg/rb/([^\']+)')
m = p.search(r.content)
Url = m.group()

DownloadImageFile(Url)

