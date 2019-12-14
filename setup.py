#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
import cat


if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.2+ to use random-cat.")


description = "Modul/Command Line Tool to get dog images"
cur_dir = os.path.dirname(__file__)
try:
    with open(os.path.join(cur_dir, 'README.md')) as file:
        long_description = file.read()
except:
    long_description = description

setup(
    name = "random-dog",
    version = cat.__version__,
    url = 'https://github.com/Prasnal/random-cat',
    license = 'MIT',
    description = description,
    long_description = long_description,
    author = 'krasncatal',
    author_email = 'krasnal@lisp.pl',
    keywords = 'dog fun',
    packages = find_packages(),
    entry_points="""
    [console_scripts]
    randomdog = dog:main
    """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Topic :: Terminals',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Artistic Software',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ]
)
