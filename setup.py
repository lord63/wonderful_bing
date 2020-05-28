#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from wonderful_bing import __version__

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()

setup(
    name='wonderful_bing',
    version=__version__,
    description="A script download Bing's img and set as wallpaper",
    long_description=long_description,
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='bing wallpaper',
    packages=['wonderful_bing'],
    install_requires=['docopt>=0.6.2', 'requests>=2.4.0'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bing=wonderful_bing.wonderful_bing:main']
    }
)
