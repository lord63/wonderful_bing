Wonderful\_Bing
===============

|Latest Version| |The MIT License| |Platform|

Requirements
------------

-  Linux platform
-  Python 2.7
-  Requests lib

Usage
-----

-  You need to set a directory to save the downloaded pictures, end with
   ‘/’.

   ::

       $ wonderful_bing -d /path/to/save/pictures/

Snapshots
---------

the first time you run it:

::

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    Successfully download the picture to --> /home/lord63/pictures/bing/CascadePools.jpg
    Successfully set the picture as the wallpaper. :)

if you don’t set the directory:

::

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    Set the directory to save Bing's imgs first.
    For more information, use --help.

if the picture has been downloaded before:

::

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    You have downloaded the picture before.
    Have a look at it --> /home/lord63/pictures/bing/CascadePools.jpg

if your pc doesn’t connect to the network, it will try again after 5
mins.

::

    $ python wonderful_bing.py -d /home/lord63/pictures/bing/
    ConnectionError,check your network please.
    Will try again after 5 minutes.


License
-------

MIT License

.. |Latest Version| image:: http://img.shields.io/pypi/v/wonderful_bing.svg
   :target: https://pypi.python.org/pypi/wonderful_bing
.. |The MIT License| image:: http://img.shields.io/badge/license-MIT-yellow.svg
   :target: https://github.com/lord63/wonderful_bing/blob/master/LICENSE
.. |Platform| image:: http://img.shields.io/badge/Platform-Linux-orange.svg