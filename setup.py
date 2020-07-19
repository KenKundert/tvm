#!/usr/bin/env python

from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'tvm',
    version = '0.5.0',
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
    keywords='money interest loans savings annuity financial'.split(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: Financial',
    ],
)
