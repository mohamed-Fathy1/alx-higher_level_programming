#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''
from urllib import parse
from urllib.request import Request, urlopen
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
