from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='wonderful_bing',
    version='0.4.0',
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
    ],
    keywords='bing wallpaper',
    packages=['wonderful_bing'],
    install_requires=['requests'],
    package_data={
        'wonderful_bing': ['README.rst', 'LICENSE', 'img/icon.png', 'img/notify.png'],
    },
    entry_points={
        'console_scripts': [
            'wonderful_bing=wonderful_bing.wonderful_bing:main']
    }
    )
