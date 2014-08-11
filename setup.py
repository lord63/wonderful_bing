#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys

try:
    from pypandoc import convert
    readme_md = lambda f: convert(f, 'rst')
except ImportError:
    sys.exit("Please install pypandoc.")
except OSError:
    sys.exit("You probably do not have pandoc installed.")


setup(
    name='wonderful_bing',
    version='0.4.1',
    description="A script download Bing's img and set as wallpaper",
    long_description=readme_md('README.md'),
    url='https://github.com/lord63/wonderful_bing',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='bing wallpaper',
    packages=['wonderful_bing'],
    install_requires=['requests'],
    package_data={
        'wonderful_bing': ['README.md', 'LICENSE', 'img/icon.png', 'img/notify.png'],
    },
    entry_points={
        'console_scripts': [
            'wonderful_bing=wonderful_bing.wonderful_bing:main']
    }
)
