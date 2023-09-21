#!/usr/bin/python3
'''
Write a Python script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        # content_type = response.headers.get(
        # "Content-Type").split("charset=")[-1]
        print('Body response:')
        print(f'\t- type: {type(response.msg.encode())}')
        print(f'\t- content: {response.msg.encode()}')
        print(
            f'\t- utf8 content: {response.msg}')
