#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    res = r.json()
    i = 0
    while 10 > i < len(res):
        print("{}: {}".format(
                res[i].get("sha"),
                res[i].get("commit").get("author").get("name")))
        i += 1
