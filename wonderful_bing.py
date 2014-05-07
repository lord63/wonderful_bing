#!/usr/bin/env python

import re
import time
import os
import gtk
import gobject
import pygtk
pygtk.require("2.0")
import pynotify
pynotify.init('Wonderful_Bing')

import requests
from lxml import html


class Wonderful_Bing():
    def __init__(self):
        self.tooltip = "Wonderful_Bing\nWait..."
        self.total = 0
        self.init_icon()
        self.notifier = pynotify.Notification("Wonderful_Bing")
        self.update()
        gobject.timeout_add(3, self.on_quit)

    def right_click(self, icon, button, time):
        self.menu.popup(None, None, None, button, time)
        return False

    def init_icon(self):
        self.icon = gtk.status_icon_new_from_stock(gtk.STOCK_FIND)
        self.icon.set_title("Wonderful_Bing")
        self.icon.set_tooltip(self.tooltip)
        self.icon.set_visible(True)
        # Add a menu for the icon
        self.menu = gtk.Menu()
        quit = gtk.MenuItem("Quit")
        quit.connect("activate", gtk.main_quit)
        self.menu.append(quit)
        self.menu.show_all()
        self.icon.connect("popup-menu", self.right_click)

    def update(self):
        def get_info(self):
            r = requests.get('http://cn.bing.com')
            tree = html.fromstring(r.text)
            info1 = tree.xpath('//div[@id="hp_pgm0"]/h3/text()')[0]
            info2 = tree.xpath('//div[@id="hp_pgm0"]/a/text()')[0]
            return info1+'\n'+info2
        info = get_info(self) 
        self.tooltip = info
        self.icon.set_tooltip(self.tooltip)
        self.notifier.update("Wonderful_Bing", self.tooltip, "dialog-warning")
        self.notifier.show()
        return True

    def on_quit(self):
        gtk.main_quit()


def get_picture_url(page_url):
    r = requests.get(page_url)
    match = re.search(
        "(?<=')http://s.cn.bing.net/az/hprichbg/rb/.+?(?=')", r.text)
    picture_url = match.group()
    return picture_url


def download_and_set(picture_url):
    picture_name = get_picture_name(picture_url)
    picture_path = "/home/lord63/pictures/bing/" + picture_name
    if os.path.exists(picture_path):
        print "You have downloaded the picture before."
        print "Have a look at it --> " + picture_path
        return

    r = requests.get(picture_url, stream=True)  # To get the raw content
    with open(picture_path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    print "Successfully download the picture to --> " + picture_path
    set_wallpaper(picture_path)
    print "Successfully set the picture as the wallpaper. :)"
    nm = Wonderful_Bing()
    gtk.main()


def get_picture_name(picture_url):
    match = re.search(
        "(?<=http://s.cn.bing.net/az/hprichbg/rb/).+?(?=_)", picture_url)
    picture_name = match.group() + '.jpg'
    return picture_name


def set_wallpaper(picture_path):
    os.system('gsettings set org.gnome.desktop.background picture-uri file:' +
              picture_path)


def main():
    picture_url = get_picture_url("http://cn.bing.com")
    download_and_set(picture_url)


# ----------------------------------------------------------------------#

# sleep for five seconds, otherwise the newly setted wallpaper will be
# setted back by the system when your system boots up if you have added
# this script to autostart.
time.sleep(5)
print "Program start"
try:
    main()
except requests.exceptions.ConnectionError:
    print "ConnectionError,check your network please."
    time.sleep(300)
    main()
print "Program end"