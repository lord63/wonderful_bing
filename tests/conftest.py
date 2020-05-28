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
        url=('https://www.bing.com/th?id=OHR.OldManWhiskers_ZH-CN9321160932_'
             '1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'),
        status=200,
        body='Hello, world'
    )

    responses.start()
    yield responses
    responses.stop()
