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
    for commit in res[:10]:
        print(f'{commit.get("sha")}: \
{commit.get("commit").get("author").get("name")}')