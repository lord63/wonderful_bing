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
        bing = WonderfulBing(self.arguments)
        self.assertIsNotNone(bing.copyright)
        self.assertIsNotNone(bing.picture_url)

    def test_get_picture_name(self):
        wonderful_bing = WonderfulBing(self.arguments)
        picture_name = wonderful_bing.get_picture_name()
        self.assertIsNotNone(picture_name)

    def test_picture_has_been_downloaded(self):
        command = "bing set -d {0} {1}".format(
            self.directory, self.arguments['ENVIRONMENT'])
        call(command.split())
        call(command.split())
        picture_has_been_downloaded_status = call(command.split())
        self.assertEqual(picture_has_been_downloaded_status, 0)

    def test_without_directory(self):
        command = "bing set {0}".format(self.arguments['ENVIRONMENT'])
        no_dir_specified_status = call(command.split())
        self.assertEqual(no_dir_specified_status, 0)

    def test_directory_not_exist(self):
        command = "bing -d {0} {1}".format(self.not_exist_dir,
                                           self.arguments['ENVIRONMENT'])
        dir_not_exist_status = call(command.split())
        self.assertEqual(dir_not_exist_status, 1)

    def test_common_command(self):
        help_message_status = call(['bing', '-h'])
        version_status = call(['bing', '--version'])
        dir_specified_status = call([
            'bing', 'set',
            '-d', '{}'.format(self.directory),
            '{}'.format(self.arguments['ENVIRONMENT'])])
        self.assertEqual(version_status, 0)
        self.assertEqual(help_message_status, 0)
        self.assertEqual(dir_specified_status, 0)

    def test_story(self):
        story_status = call(['bing', 'story'])
        self.assertEqual(story_status, 0)


if __name__ == '__main__':
    unittest.main()
