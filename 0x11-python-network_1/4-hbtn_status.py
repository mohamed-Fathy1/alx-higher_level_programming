#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type:', type(response.reason))
print('\t- content:', response.reason)
