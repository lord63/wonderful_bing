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
__version__ = "0.6.1"
__author__ = "lord63"
__license__ = "MIT"
__copyright__ = "Copyright 2014 lord63"

import re
import time
import sys
from os import path
import subprocess

import requests
from docopt import docopt


class WonderfulBing(object):
    def __init__(self, arguments):
        # Get all the information we need from this url, see issue#7
        self.url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=\
                   1&nc=1409879295618&pid=hp"
        information = requests.get(self.url).json()["images"][0]
        self.copyright = information["copyright"]
        self.picture_url = information["url"]
        if not self.picture_url.startswith('http'):
            self.picture_url = 'http://www.bing.com' + self.picture_url
        self.environment = arguments['ENVIRONMENT']
        self.directory = path.abspath(arguments['--directory']) + '/'

    def show_notify(self):
        """show the notify to get to know the picture story"""
        title = "Today's Picture Story"
        story_content = re.match(
            ".+(?=\(\xa9)", self.copyright).group().encode('utf-8')
        notify_icon = path.dirname(path.realpath(__file__)) + '/img/icon.png'
        safe_story_content = story_content.replace('"', '\"')
        subprocess.Popen(["notify-send", "-a", "wonderful_bing", "-i",
                          notify_icon, title, safe_story_content])

    def get_picture_name(self):
        """get a nice picture name from the download url"""
        match = re.search(
            "(?<=/az/hprichbg/rb/).+?(?=_)", self.picture_url)
        picture_name = match.group() + '.jpg'
        return picture_name

    def set_wallpaper(self, picture_path):  # pragma: no cover
        # We use this command to make it work when using cron, see #3
        if self.environment in ['gnome', 'gnome2', 'cinnamon']:
            status = subprocess.Popen(
                "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set \
                org.gnome.desktop.background picture-uri file://{0}".format(
                    picture_path), shell=True)
        elif self.environment == 'xfce4':
            status = subprocess.Popen(
                "DISPLAY=:0 xfconf-query -c xfce4-desktop -p \
                /backdrop/screen0/monitor0/image-path -s {0}".format(
                    picture_path), shell=True)
        else:
            sys.exit(
                "Currently we don't support your desktop_environment.\n"
                "Please file an issue or make a pull request :) \n"
                "https://github.com/lord63/wonderful_bing")
        if status.wait() == 0:
            print "Successfully set the picture as the wallpaper. :)"
        else:
            print "Something bad happened, fail to set as wallpaper :("

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
        self.show_notify()


def main():
    doc = """
A wallpaper a day, keep the doctor away.

Usage:
  bing set [-d DIRECTORY] ENVIRONMENT
  bing story
  bing -V | --version
  bing -h | --help

Arguments:
  ENVIRONMENT                your desktop environment

Options:
  -h, --help                 show the help info and exit
  -V, --version              show the version and exit
  -d, --directory=DIRECTORY  specify where to save the download picture
                             [default: /tmp]

"""
    arguments = docopt(doc, version=__version__)
    if not path.exists(arguments['--directory']):
        sys.exit('No such directory :(')

    bing = WonderfulBing(arguments)
    try:
        if arguments['story']:
            print bing.copyright
        else:
            bing.download_and_set()
    except requests.exceptions.ConnectionError:
        print "ConnectionError,check your network please."
        print "Will try again after 5 minutes."
        time.sleep(300)
        bing.download_and_set()


if __name__ == '__main__':
    main()
