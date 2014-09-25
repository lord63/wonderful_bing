#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import call

from wonderful_bing.wonderful_bing import WonderfulBing

class WonderfulBingTestCase(unittest.TestCase):
    def setUp(self):
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.current_dir_with_slash = self.current_dir + '/'
        self.not_exist_dir = '/test/'

    def tearDown(self):
        """delete the download picture"""
        for root, dirs, files in os.walk(self.current_dir_with_slash):
            for file in files:
                if file.endswith('.jpg'):
                    os.remove(file)

    def test_initial(self):
        print "\n----------test_initial begin----------"
        wonderful_bing = WonderfulBing(
            {'directory': self.current_dir_with_slash})
        assert wonderful_bing.copyright
        assert wonderful_bing.picture_url
        print "----------test_initial end----------"

    def test_get_picture_name(self):
        print "\n----------test_get_picture_name begin----------"
        wonderful_bing = WonderfulBing(
            {'directory': self.current_dir_with_slash})
        picture_name = wonderful_bing.get_picture_name()
        assert picture_name
        print "----------test_get_picture_name end----------"

    def test_common_command(self):
        print "\n----------test_common_command begin----------"
        help_message_status = call([
            'python', './wonderful_bing/wonderful_bing.py', '-h'])
        version_status = call(['python', './wonderful_bing/wonderful_bing.py',
                               '-V'])
        dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.current_dir_with_slash)])
        assert not version_status
        assert not help_message_status
        assert not dir_specified_status
        print "----------test_common_command end----------"

    def test_picture_has_been_downloaded(self):
        print "\n----------test_picture_has_been_downloaded begin----------"
        call(['python', './wonderful_bing/wonderful_bing.py',
              '-d', '{}'.format(self.current_dir_with_slash)])
        picture_has_been_downloaded_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.current_dir_with_slash)])
        assert not picture_has_been_downloaded_status
        print "----------test_picture_has_been_downloaded end----------"

    def test_without_directory(self):
        print "\n----------test_without_directory begin----------"
        no_dir_specified_status = call([
            'python', './wonderful_bing/wonderful_bing.py'])
        assert no_dir_specified_status
        print "----------test_without_directory end----------"

    def test_directory_not_exist(self):
        print "\n----------test_directory_not_exist begin----------"
        dir_not_exist_status = call([
            'python', './wonderful_bing/wonderful_bing.py',
            '-d', '{}'.format(self.not_exist_dir)])
        assert dir_not_exist_status
        print "----------test_directory_not_exist end----------"


if __name__ == '__main__':
    unittest.main()
