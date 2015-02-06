#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import call

from wonderful_bing.wonderful_bing import WonderfulBing


class WonderfulBingTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = '/tmp/'
        self.not_exist_dir = '/notexist/'
        self.arguments = {'--directory': self.directory,
                          'ENVIRONMENT': 'gnome'}

    def tearDown(self):
        """delete the download picture"""
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.jpg'):
                    os.remove(self.directory + file)

    def test_initial(self):
        wonderful_bing = WonderfulBing(self.arguments)
        assert wonderful_bing.copyright
        assert wonderful_bing.picture_url

    def test_get_picture_name(self):
        wonderful_bing = WonderfulBing(self.arguments)
        picture_name = wonderful_bing.get_picture_name()
        assert picture_name

    def test_picture_has_been_downloaded(self):
        command = "python ./wonderful_bing/wonderful_bing.py set -d \
            {0} {1}".format(self.directory, self.arguments['ENVIRONMENT'])
        call(command.split())
        picture_has_been_downloaded_status = call(command.split())
        assert not picture_has_been_downloaded_status

    def test_without_directory(self):
        command = "python ./wonderful_bing/wonderful_bing.py set {0}".format(
            self.arguments['ENVIRONMENT'])
        no_dir_specified_status = call(command.split())
        assert not no_dir_specified_status

    def test_directory_not_exist(self):
        command = "python ./wonderful_bing/wonderful_bing.py set -d \
            {0} {1}".format(self.not_exist_dir, self.arguments['ENVIRONMENT'])
        dir_not_exist_status = call(command.split())
        assert dir_not_exist_status

    def test_common_command(self):
        help_message_status = call([
            'python', './wonderful_bing/wonderful_bing.py', '-h'])
        version_status = call(['python', './wonderful_bing/wonderful_bing.py',
                               '--version'])
        dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py', 'set',
            '-d', '{}'.format(self.directory),
            '{}'.format(self.arguments['ENVIRONMENT'])])
        assert not version_status
        assert not help_message_status
        assert not dir_specified_status

if __name__ == '__main__':
    unittest.main()
