#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path

import mock
import pytest

from wonderful_bing.wonderful_bing import WonderfulBing


@pytest.mark.usefixtures('mock_request')
def test_picture_has_be_downloaded():
    with mock.patch('os.path.exists', return_value=True):
        with pytest.raises(SystemExit):
            arguments = {'--directory': '/not/exist', 'ENVIRONMENT': 'gnome'}
            wonderful_bing = WonderfulBing(arguments)
            wonderful_bing.download_picture()


@pytest.mark.usefixtures('mock_request')
def test_download_picture():
    arguments = {'--directory': '/tmp', 'ENVIRONMENT': 'gnome'}
    wonderful_bing = WonderfulBing(arguments)
    check_picture(wonderful_bing.picture_path)
    with mock.patch('time.sleep', return_value=None):
        wonderful_bing.download_picture()
    assert path.exists(wonderful_bing.picture_path)
    check_picture(wonderful_bing.picture_path)


def check_picture(picture_path):
    if path.exists(picture_path):
        os.remove(picture_path)
