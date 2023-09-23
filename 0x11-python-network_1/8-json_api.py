#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {'q': argv[1] if len(argv) > 1 else ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        res = response.json()
        if isinstance(res, dict):
            if res:
                print(f"[{res['id']}] {res['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
