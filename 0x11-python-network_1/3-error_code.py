#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
'''
from urllib.request import HTTPError, urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as res:
            print(res.read())
    except HTTPError as e:
        print(e.code)
