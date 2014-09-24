#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import call

from wonderful_bing.wonderful_bing import WonderfulBing

class WonderfulBingTestCase(unittest.TestCase):

    def setUp(self):
        self.current_directory = os.path.abspath(os.path.dirname(__file__))
        self.directory_with_slash = self.current_directory + '/'

    def tearDown(self):
        """delete the download picture"""
        for root, dirs, files in os.walk(self.current_directory):
            for file in files:
                if file.endswith('.jpg'):
                    os.remove(file)

    def test_initial(self):
        wonderful_bing = WonderfulBing({'directory': self.directory_with_slash})
        assert wonderful_bing.copyright
        assert wonderful_bing.picture_url

    def test_get_picture_name(self):
        wonderful_bing = WonderfulBing({'directory': self.directory_with_slash})
        picture_name = wonderful_bing.get_picture_name()
        assert picture_name

    def test_command(self):
        help_message_status = call([
            'python', './wonderful_bing/wonderful_bing.py', '-h'])
        version_status = call(['python', './wonderful_bing/wonderful_bing.py',
                                '-V'])
        no_dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py'])
        dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.directory_with_slash)])
        assert not version_status
        assert not help_message_status
        assert no_dir_specified_status
        assert not dir_specified_status

    def test_picture_has_been_downloaded(self):
        dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.directory_with_slash)])
        picture_has_been_downloaded_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.directory_with_slash)])
        assert not picture_has_been_downloaded_status

if __name__ == '__main__':
    unittest.main()
