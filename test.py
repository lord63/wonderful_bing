#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import call

from wonderful_bing.wonderful_bing import WonderfulBing


class WonderfulBingTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = os.path.abspath(os.path.dirname(__file__))
        self.not_exist_dir = '/test/'

    def tearDown(self):
        """delete the download picture"""
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.jpg'):
                    os.remove(os.path.abspath(file))

    def test_initial(self):
        wonderful_bing = WonderfulBing(
            {'directory': self.directory})
        assert wonderful_bing.copyright
        assert wonderful_bing.picture_url

    def test_get_picture_name(self):
        wonderful_bing = WonderfulBing(
            {'directory': self.directory})
        picture_name = wonderful_bing.get_picture_name()
        assert picture_name

    def test_common_command(self):
        help_message_status = call([
            'python', './wonderful_bing/wonderful_bing.py', '-h'])
        version_status = call(['python', './wonderful_bing/wonderful_bing.py',
                               '-V'])
        dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.directory)])
        assert not version_status
        assert not help_message_status
        assert dir_specified_status

    def test_picture_has_been_downloaded(self):
        call(['python', './wonderful_bing/wonderful_bing.py',
              '-d', '{}'.format(self.directory)])
        picture_has_been_downloaded_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.directory)])
        assert not picture_has_been_downloaded_status

    def test_without_directory(self):
        no_dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py'])
        assert no_dir_specified_status

    def test_directory_not_exist(self):
        dir_not_exist_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.not_exist_dir)])
        assert dir_not_exist_status

if __name__ == '__main__':
    unittest.main()
