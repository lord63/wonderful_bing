#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests


class WonderfulBing(object):
    def __init__(self, url, redirects=True):
        self.url = url
        self.response = requests.get(url, allow_redirects=redirects)

    def test_picture_url(self):
        picture_url = re.search(
            "/az/hprichbg/rb/.+?(?=')", self.response.text).group()
        return picture_url

    def test_picture_name(self, picture_url):
        picture_name = re.search(
            "(?<=/az/hprichbg/rb/).+?(?=_)", picture_url).group()
        return picture_name

    def test_story_name(self):
        story_name = re.search(
            '((?<=id="sh_cp" title=")|\
            (?<=class="sc_light" title=")).*(?=\(\\xa9)',
            self.response.text).group()
        return story_name


def test_ZH():
    bing_ZH = WonderfulBing('http://cn.bing.com')
    picture_url = bing_ZH.test_picture_url()
    assert picture_url
    assert bing_ZH.test_picture_name(picture_url)
    assert bing_ZH.test_story_name()


def test_EN():
    bing_EN = WonderfulBing('http://www.bing.com', False)
    picture_url = bing_EN.test_picture_url()
    assert picture_url
    assert bing_EN.test_picture_name(picture_url)
    assert bing_EN.test_story_name()
