#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json
from os import path

import pytest
import responses


@pytest.yield_fixture
def mock_request():
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
    responses.add(
        responses.GET,
        url=("https://www.bing.com/az/hprichbg/rb/HudsonBayPolars_"
             "ZH-CN10500767857_1920x1080.jpg"),
        status=200,
        body='Hello, world'
    )

    responses.start()
    yield responses
    responses.stop()
