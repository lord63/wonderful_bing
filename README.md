# Wonderful_Bing

[![Latest Version][1]][2]
[![Build Status][3]][4]
![Platform][5]

## Requirements

* Linux platform
* Python 2.7
* Requests lib
* python-notify

## Install

    $ sudo pip install wonderful_bing
    $ sudo apt-get install python-notify

## Usage

* Manually

You need to set a directory to save the download pictures, end with '/'.

    $ wonderful_bing -d /path/to/save/pictures/

* Automatically(recommand)

1. Add it to `startup application`(in my Linux Mint16), then every time you boot
up your pc, this script will automatically run for you.

2. Or use `cron`. Let me give you an example:

        0 8 * * * env DISPLAY=:0 /usr/local/bin/wonderful_bing -d /home/lord63/pictures/bing/

*we need `env DISPLAY=:0`, otherwise the notify can't display at all, and remember
the `/` at the end.*

3. Or use `anacron`, but the original `anacron` will run the script in root, thus
it may fail in setting the picture to wallpaper. Follow [this][6] to let you run
`anacron` as normal user. Let me give you an example, add the following line in
`$HOME/.anacron/anacrontab`:

        1 1 wonderful_bing env DISPLAY=:0 /usr/local/bin/wonderful_bing -d /home/lord63/pictures/bing/

If you find a better way, please let me know :)

## Snapshots

the first time you run it:

    $ wonderful_bing -d /home/lord63/pictures/bing/
    Successfully download the picture to --> /home/lord63/pictures/bing/CascadePools.jpg
    Successfully set the picture as the wallpaper. :)

if you don't set the directory:

    $ wonderful_bing -d /home/lord63/pictures/bing/
    Set the directory to save Bing's imgs first.
    For more information, use --help.


if the picture has been downloaded before:

    $ wonderful_bing -d /home/lord63/pictures/bing/
    You have downloaded the picture before.
    Have a look at it --> /home/lord63/pictures/bing/CascadePools.jpg

if your pc doesn't connect to the network, it will try again after 5 mins.

    $ wonderful_bing -d /home/lord63/pictures/bing/
    ConnectionError,check your network please.
    Will try again after 5 minutes.

and the notify should looks like this:

![](./wonderful_bing/img/notify.png)

## License

MIT License


[1]: http://img.shields.io/pypi/v/wonderful_bing.svg
[2]: https://pypi.python.org/pypi/wonderful_bing
[3]: https://travis-ci.org/lord63/wonderful_bing.svg
[4]: https://travis-ci.org/lord63/wonderful_bing
[5]: http://img.shields.io/badge/Platform-Linux-blue.svg
[6]: http://www.wellengang.ch/?p=135
