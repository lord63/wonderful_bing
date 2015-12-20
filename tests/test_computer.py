#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from os import path

import mock
import pytest

from wonderful_bing.wonderful_bing import Computer


@pytest.fixture
def computer():
    computer = Computer()
    return computer


def test_computer(computer):
    gnome_based = ("DISPLAY=:0 GSETTINGS_BACKEND=dconf "
                   "/usr/bin/gsettings set org.gnome.desktop.background "
                   "picture-uri file://{0}")
    mate_based = ("DISPLAY=:0 GSETTINGS_BACKEND=dconf "
                  "/usr/bin/gsettings set org.mate.background "
                  "picture-filename '{0}'")
    xfce_based = ("DISPLAY=:0 xfconf-query -c xfce4-desktop "
                  "-p /backdrop/screen0/monitor0/image-path -s {0}")

    assert computer._get_command('gnome') == gnome_based
    assert computer._get_command('gnome2') == gnome_based
    assert computer._get_command('cinnamon') == gnome_based
    assert computer._get_command('mate') == mate_based
    assert computer._get_command('xfce4') == xfce_based
    assert computer._get_command('blablabla') is None


def test_set_wallpaper_with_unsupported_environment(computer):
    with pytest.raises(SystemExit):
        computer.set_wallpaper('blablabla', 'tmp/blabla.jpg')


def test_set_wallpaper(computer):
    with mock.patch('wonderful_bing.wonderful_bing.subprocess') as subprocess:
        subprocess.Popen.return_value.returncode = 0
        computer.set_wallpaper('gnome', '/tmp/blabla.jpg')
        command = computer._get_command('gnome').format('/tmp/blabla.jpg')
        subprocess.Popen.assert_called_once_with(command, shell=True)


def test_show_notify(computer):
    with mock.patch('wonderful_bing.wonderful_bing.subprocess') as subprocess:
        computer.show_notify('Hello, world')
        notify_icon = path.join(
            path.dirname(path.dirname(path.realpath(__file__))),
            'wonderful_bing/img/icon.png')
        subprocess.Popen.assert_called_once_with(
            ["notify-send", "-a", "wonderful_bing", "-i",
             notify_icon, "Today's Picture Story", "Hello, world"])
