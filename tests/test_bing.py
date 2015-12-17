#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os import path

import responses

from wonderful_bing.wonderful_bing import Bing


@responses.activate
def test_bing():
    with open(path.join(path.dirname(path.realpath(__file__)),
                        'fake_response.json')) as f:
        fake_response = json.load(f)

    responses.add(
        responses.GET,
        url=("https://www.bing.com/HPImageArchive.aspx?format"
             "=js&idx=0&n=1&nc=1409879295618&pid=hp"),
        json=fake_response,
        status=200,
        match_querystring=True
    )

    bing = Bing()
    assert bing.url == ("https://www.bing.com/HPImageArchive.aspx?format=js"
                        "&idx=0&n=1&nc=1409879295618&pid=hp")
    assert bing.picture_name == 'HudsonBayPolars.jpg'
    assert bing.picture_story == (u'加拿大，结冰的哈德逊湾，北极熊妈妈'
                                  u'和她的宝宝  (© Kike Calvo/Corbis)')
    assert bing.picture_url == ('https://www.bing.com/az/hprichbg/rb/Hudson'
                                'BayPolars_ZH-CN10500767857_1920x1080.jpg')
