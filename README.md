# Wonderful_Bing

[![Latest Version][1]][2]
[![The MIT License][3]][4]
![Platform][5]


## Requirements


* Linux platform
* Python 2.7
* Requests lib


## Usage

* Manually

You need to set a directory to save the download pictures, end with '/'.

    $ wonderful_bing -d /path/to/save/pictures/

* Automatically(recommand)

1. Add it to `startup application`(in my Linux Mint16), then every time you boot 
up your pc, this script will automatically run for you.

2. Use cron. Let me give you an example:

> 0 8 * * * env DISPLAY=:0 /usr/local/bin/wonderful_bing -d /path/to/save/

*we need `env DISPLAY=:0`, otherwise the notify can't display at all, and remember
the `/` at the end.*

## Snapshots

the first time you run it:

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    Successfully download the picture to --> /home/lord63/pictures/bing/CascadePools.jpg
    Successfully set the picture as the wallpaper. :)

if you don't set the directory:

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    Set the directory to save Bing's imgs first.
    For more information, use --help.


if the picture has been downloaded before:

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    You have downloaded the picture before.
    Have a look at it --> /home/lord63/pictures/bing/CascadePools.jpg

if your pc doesn't connect to the network, it will try again after 5 mins.

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    ConnectionError,check your network please.
    Will try again after 5 minutes.

and the notify should looks like this:

![](./wonderful_bing/img/notify.png)


## License

MIT License


[1]: http://img.shields.io/pypi/v/wonderful_bing.svg
[2]: https://pypi.python.org/pypi/wonderful_bing
[3]: http://img.shields.io/badge/license-MIT-yellow.svg
[4]: https://github.com/lord63/wonderful_bing/blob/master/LICENSE
[5]: http://img.shields.io/badge/Platform-Linux-orange.svg
