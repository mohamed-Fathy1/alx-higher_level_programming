#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])

    if response.ok:
        print(response.text)
    else:
        print('Error code:', response.status_code)
