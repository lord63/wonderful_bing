# -*- coding=utf-8 -*-
import re
import requests


def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    print "Download Image File=", local_filename
    r = requests.get(imgUrl, stream=True)
    with open("/home/lord63/pictures/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
    return local_filename


r = requests.get('http://cn.bing.com')

p = re.compile('http://s.cn.bing.net/az/hprichbg/rb/[^\']+')
m = p.search(r.content)

Url = m.group()
downloadImageFile(Url)

