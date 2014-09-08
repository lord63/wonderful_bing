#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import unittest
from subprocess import Popen
from subprocess import call

from wonderful_bing.wonderful_bing import WonderfulBing

current_directory = os.path.abspath(os.path.dirname(__file__))
directory_with_slash = current_directory + '/'


def test_initial():
    wonderful_bing = WonderfulBing({'directory': directory_with_slash})
    assert wonderful_bing.copyright
    assert wonderful_bing.picture_url

def test_command():
    help_message_status = call([
        'python', './wonderful_bing/wonderful_bing.py', '-h'])
    version_status = call(['python', './wonderful_bing/wonderful_bing.py',
                            '-V'])
    no_dir_specified_status = call([
        'python', './wonderful_bing/wonderful_bing.py'])
    dir_specified_status = call([
        'python', './wonderful_bing/wonderful_bing.py',
        '-d', '{}'.format(directory_with_slash)])
    assert not version_status
    assert not help_message_status
    assert no_dir_specified_status
    assert not dir_specified_status
