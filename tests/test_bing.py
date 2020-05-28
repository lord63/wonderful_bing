#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os import path

import pytest

from wonderful_bing.wonderful_bing import Bing


@pytest.mark.usefixtures('mock_request')
def test_bing():
    bing = Bing()
    assert bing.url == ("https://www.bing.com/HPImageArchive.aspx?format=js"
                        "&idx=0&n=1&nc=1409879295618&pid=hp")
    assert bing.picture_name == 'OldManWhiskers.jpg'
    assert bing.picture_story == (u'结籽时的三花锦葵的长羽 '
                                  u'(© Sunshine Haven Photo/Shutterstock)')
    assert bing.picture_url == (
        'https://www.bing.com/th?id=OHR.OldManWhiskers_ZH-CN9321160932_'
        '1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp')
