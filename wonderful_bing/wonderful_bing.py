#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    wonderful_bing
    ~~~~~~~~~~~~~~

    Wonderful_bing is a small and simple program that helps you download
    pictures from Bing and set as wallpaper. My first python program :)

    :copyright: (c) 2014 by lord63.
    :license: MIT, see LICENSE for more details.
"""

__title__ = "wonderful_bing"
__version__ = "0.5.0"
__author__ = "lord63"
__license__ = "MIT"
__copyright__ = "Copyright 2014 lord63"

import re
import time
import os
import sys
from os import path
import argparse

import requests


class WonderfulBing(object):
    def __init__(self, config):
        # Get all the information we need from this url, see issue#7
        self.url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=\
                   1&nc=1409879295618&pid=hp"
        information = requests.get(self.url).json()["images"][0]
        self.copyright = information["copyright"]
        self.picture_url = information["url"]
        if not self.picture_url.startswith('http'):
            self.picture_url = 'http://www.bing.com' + self.picture_url
        self.directory = config['directory']

    def show_notify(self):
        """show the notify to get to know the picture story"""
        title = "Today\\'s\ Picture\ Story"
        story_content = re.match(
            ".+(?=\(\xa9)", self.copyright).group().encode('utf-8')
        notify_icon = path.dirname(path.realpath(__file__)) + '/img/icon.png'
        os.system("notify-send -a wonderful_bing -i {0} {1} '{2}'".format(
                  notify_icon, title, story_content))

    def get_picture_name(self):
        """get a nice picture name from the download url"""
        match = re.search(
            "(?<=/az/hprichbg/rb/).+?(?=_)", self.picture_url)
        picture_name = match.group() + '.jpg'
        return picture_name

    def set_wallpaper(self, picture_path):
        # We use this command to make it work when using cron, see #3
        os.system('DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings \
                  set org.gnome.desktop.background picture-uri file://' +
                  picture_path)

    def download_and_set(self):
        picture_name = self.get_picture_name()
        picture_path = self.directory + picture_name
        if path.exists(picture_path):
            print "You have downloaded the picture before."
            print "Have a look at it --> {0}".format(picture_path)
            sys.exit()
        # Sleep for two seconds, otherwise the newly setted wallpaper
        # will be setted back by the system when your system boots up
        # if you have added this script to autostart.
        time.sleep(2)
        # Set stream to true to get the raw content
        request = requests.get(self.picture_url, stream=True)
        with open(picture_path, "wb") as f:
            for chunk in request.iter_content(1024):
                f.write(chunk)
        print "Successfully download the picture to --> {0}.".format(
            picture_path)
        self.set_wallpaper(picture_path)
        print "Successfully set the picture as the wallpaper. :)"
        self.show_notify()


def main():
    parser = argparse.ArgumentParser(
        prog='wonderful_bing',
        description="Wonderful_bing's configuration")
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {0}'.format(__version__))
    parser.add_argument(
        '-d', dest='directory',
        help="set the directory to save Bing's imgs, end with '/'")
    config = vars(parser.parse_args())
    if not config['directory']:
        sys.exit("Set the directory to save Bing's imgs first.\n"
                 "For more information, use --help.")
    if not config['directory'].endswith('/'):
        config['directory'] = config['directory'] + '/'
    if not path.exists(config['directory']):
        sys.exit('No such directory :(')

    bing = WonderfulBing(config)
    try:
        bing.download_and_set()
    except requests.exceptions.ConnectionError:
        print "ConnectionError,check your network please."
        print "Will try again after 5 minutes."
        time.sleep(300)
        bing.download_and_set()


if __name__ == '__main__':
    main()
