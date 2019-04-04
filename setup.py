#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name = 'tvm',
    version = '0.0.1',
    author = 'Ken Kundert',
    author_email = 'tvm@nurdletech.com',
    description = 'Time Value of Money',
    long_description = readme,
    scripts = 'tvm'.split(),
    url = 'https://github.com/kenkundert/tvm',
    download_url = 'https://github.com/kenkundert/tvm/tarball/master',
    license = 'GPLv3+',
    install_requires = 'appdirs docopt inform quantiphy'.split(),
    python_requires='>=3.6',
)
