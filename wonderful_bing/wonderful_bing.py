#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import os
import sys
import argparse
import pynotify
pynotify.init('Wonderful_Bing')

import requests


def show_notify():
    r = requests.get('http://cn.bing.com')
    title = u'今日图片故事'
    story_name = re.search('(?<=id="sh_cp" title=").*(?=\(\\xa9)', r.text).group()
    n = pynotify.Notification(title, story_name, sys.path[0]+'/img/icon.png')
    n.show()


def get_picture_url(page_url):
    r = requests.get(page_url)
    match = re.search(
        "(?<=')http://s.cn.bing.net/az/hprichbg/rb/.+?(?=')", r.text)
    picture_url = match.group()
    return picture_url


def download_and_set(picture_url):
    picture_name = get_picture_name(picture_url)
    picture_path = config['local_directory'] + picture_name
    if os.path.exists(picture_path):
        print "You have downloaded the picture before."
        print "Have a look at it --> " + picture_path
        return

    # sleep for two seconds, otherwise the newly setted wallpaper will be
    # setted back by the system when your system boots up if you have added
    # this script to autostart.
    time.sleep(2)
    r = requests.get(picture_url, stream=True)  # To get the raw content
    with open(picture_path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    print "Successfully download the picture to --> " + picture_path
    set_wallpaper(picture_path)
    print "Successfully set the picture as the wallpaper. :)"

    show_notify()


def get_picture_name(picture_url):
    match = re.search(
        "(?<=http://s.cn.bing.net/az/hprichbg/rb/).+?(?=_)", picture_url)
    picture_name = match.group() + '.jpg'
    return picture_name


def set_wallpaper(picture_path):
    os.system('gsettings set org.gnome.desktop.background picture-uri file:' +
              picture_path)


def main():
    try:
        picture_url = get_picture_url("http://cn.bing.com")
        download_and_set(picture_url)
    except requests.exceptions.ConnectionError:
        print "ConnectionError,check your network please."
        print "Will try again after 5 minutes."
        time.sleep(300)
        picture_url = get_picture_url("http://cn.bing.com")
        download_and_set(picture_url)
    except TypeError:
        print "Set the directory to save Bing's imgs first."
        print "For more information, use --help."


parser = argparse.ArgumentParser(description="Wonderful_bing's configuration")
parser.add_argument('-d', dest='local_directory',
                    help="set the directory to save Bing's imgs, end with '/'")
config=vars(parser.parse_args())

if __name__ == '__main__':
    main()
