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
__version__ = "0.5.1"
__author__ = "lord63"
__license__ = "MIT"
__copyright__ = "Copyright 2014 lord63"

import re
import time
import os
import sys
from os import path
import argparse
import subprocess

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
        self.directory = path.abspath(config['directory']) + '/'

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
        desktop_environment = self.get_desktop_environment()
        if desktop_environment in ['gnome', 'gnome2', 'cinnamon']:
            subprocess.Popen(
                "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set \
                org.gnome.desktop.background picture-uri file://{0}".format(
                    picture_path), shell=True)
        elif desktop_environment == 'xfce4':
            subprocess.Popen(
                "DISPLAY=:0 xfconf-query -c xfce4-desktop -p \
                /backdrop/screen0/monitor0/image-path -s {0}".format(
                    picture_path), shell=True)
        else:
            sys.exit(
                "Currently we don't support your desktop_environment: {} \n"
                "Please file an issue or make a pull request :) \n"
                "https://github.com/lord63/wonderful_bing".format(
                    desktop_environment))

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

    # I get this function from http://stackoverflow.com/a/21213358
    def get_desktop_environment(self):  # pragma: no cover
        # From http://stackoverflow.com/q/2035657
        # and http://ubuntuforums.org/showthread.php?t=652320
        # and http://ubuntuforums.org/showthread.php?t=652320
        # and http://ubuntuforums.org/showthread.php?t=1139057
        if sys.platform in ["win32", "cygwin"]:
            return "windows"
        elif sys.platform == "darwin":
            return "mac"
        else:  # Most likely either a POSIX system or something not much common
            desktop_session = os.environ.get("DESKTOP_SESSION")
            # Easier to match if we doesn't have  to deal with caracter cases
            if desktop_session is not None:
                desktop_session = desktop_session.lower()
                if desktop_session in ["gnome", "unity", "cinnamon", "mate",
                                       "xfce4", "lxde", "fluxbox", "blackbox",
                                       "openbox", "icewm", "jwm", "afterstep",
                                       "trinity", "kde"]:
                    return desktop_session
                # Special cases
                # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE
                # if using LXDE.
                # There is no guarantee that they will not do the same with
                # the other desktop environments.
                elif "xfce" in (desktop_session or
                                desktop_session.startswith("xubuntu")):
                    return "xfce4"
                elif desktop_session.startswith("ubuntu"):
                    return "unity"
                elif desktop_session.startswith("lubuntu"):
                    return "lxde"
                elif desktop_session.startswith("kubuntu"):
                    return "kde"
                elif desktop_session.startswith("razor"):  # e.g. razorkwin
                    return "razor-qt"
                elif desktop_session.startswith("wmaker"):  # e.g.wmaker-common
                    return "windowmaker"
            if os.environ.get('KDE_FULL_SESSION') == 'true':
                return "kde"
            elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                if "deprecated" not in os.environ.get(
                   'GNOME_DESKTOP_SESSION_ID'):
                        return "gnome2"
            # From http://ubuntuforums.org/showthread.php?t=652320
            elif self.is_running("xfce-mcs-manage"):
                return "xfce4"
            elif self.is_running("ksmserver"):
                return "kde"
        return "unknown"


    def is_running(self, process):
        # From <http://www.bloggerpolis.com/2011/05/how-to-check-if-a-
        # process-is-running-using-python/>
        # and <http://richarddingwall.name/2009/06/18/windows-
        # equivalents-of-ps-and-kill-commands/>
        try:  # Linux/Unix
            s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
        except:  # Windows
            s = subprocess.Popen(["tasklist", "/v"], stdout=subprocess.PIPE)
        for x in s.stdout:
            if re.search(process, x):
                return True
        return False


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
