#! /usr/bin/env python

import re
import time
import os
import logging

import requests


def get_picture_url(page_url):
    r = requests.get(page_url)
    match = re.search(
        "(?<=')http://s.cn.bing.net/az/hprichbg/rb/.+?(?=')", r.text)
    picture_url = match.group()
    return picture_url


def download_and_set(picture_url):
    picture_name = get_picture_name(picture_url)
    picture_path = "/home/lord63/pictures/bing/" + picture_name
    if os.path.isfile(picture_path):
        logger.info("You have downloaded the picture before.")
        logger.info("Have a look at it --> " + picture_path)
        return

    r = requests.get(picture_url, stream=True)  # To get the raw content
    with open(picture_path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    logger.info("Successfully download the picture to " + picture_path)
    set_wallpaper(picture_path)
    logger.info("Successfully set the picture as the wallpaper. :)")


def get_picture_name(picture_url):
    match = re.search(
        "(?<=http://s.cn.bing.net/az/hprichbg/rb/).+?(?=_)", picture_url)
    picture_name = match.group() + '.jpg'
    return picture_name


def set_wallpaper(picture_path):
    os.system('gsettings set org.gnome.desktop.background picture-uri file:' +
              picture_path)

# ----------------------------------------------------------------------#
logger = logging.getLogger("wonderful_bing")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("/home/lord63/code/bing/wonderful_bing.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)
# ----------------------------------------------------------------------#

# sleep for five seconds, otherwise the newly setted wallpaper will be
# setted back by the system when your system boots up if you have added
# this script to autostart.
time.sleep(5)

logger.info("Program start")

for i in range(5):
    try:
        picture_url = get_picture_url("http://cn.bing.com")
        download_and_set(picture_url)
        break
    except requests.exceptions.ConnectionError:
        logger.info("ConnectionError")
        time.sleep(120)
        i += 1

logger.info("Program end\n")