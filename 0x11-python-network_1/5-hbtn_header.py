#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print(response.headers.get('X-Request-Id'))
