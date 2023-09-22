#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

response = requests.get(argv[1])
print(response.headers.get('X-Request-Id'))
