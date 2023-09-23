#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1]))

    res = response.json()
    i = 0
    while 10 > i < len(res):
        print(f"{res[i].get('sha')}: ",
              f"{res[i].get('commit').get('author').get('name')}")
        i += 1
