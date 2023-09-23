#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f'Bearer {argv[2]}'
    }

    response = requests.post(
        'https://api.github.com/user', headers=headers)
    res = response.json()
    print(res['id'])
