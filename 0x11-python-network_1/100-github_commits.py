#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(
        f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits')
    res = response.json()
    try:
        for commit in range(10):
            print(f'{res[commit].get("sha")}: ',
                  f'{res[commit].get("commit").get("author").get("name")}')
    except IndexError:
        pass
