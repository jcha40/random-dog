#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2019, Dorota Psota <dorota@lisp.pl>
The MIT License (MIT)

This Project uses Dog API (https://dog.ceo/dog-api/).
Thanks a lot!

Project inspired on random-cat module - github: https://github.com/gravmatt/random-cat
"""


__author__ = 'Dorota Psota'
__version__ = '1.0.1'
__license__ = 'MIT'


import uuid
import os
import sys
import requests
import json

download = None
try:
    import urllib
    download = urllib.urlretrieve
except:
    import urllib.request
    download = urllib.request.urlretrieve


url = 'https://dog.ceo/api/breeds/image/random'
breed_url = 'https://dog.ceo/api/breed/{}/images/random'


def getDog(directory=None, filename=None, breed=None):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), 'jpg')
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    dog = requests.get(breed_url.format(breed)) if breed else requests.get(url)
    if dog.status_code == 404:
        raise ValueError('No dogs available of breed {}'.format(breed))
    downloadlink=json.loads(dog.text)["message"]
    download(downloadlink, savefile)
    return savefile


def main():
    filename = None
    directory = None
    breed = None
    if(len(sys.argv) > 1):
        if sys.argv[1] == '--breed':
            breed = sys.argv[2]
        else:
            if len(sys.argv) > 2 and sys.argv[2] == '--breed':
                breed = sys.argv[3]
            filename = sys.argv[1]
            directory = os.path.sep.join(filename.split(os.path.sep)[:-1])
            filename = os.path.basename(filename).split('.')[0]
        
    sys.stdout.write(getDog(directory, filename, breed))


if __name__ == '__main__':
    main()
