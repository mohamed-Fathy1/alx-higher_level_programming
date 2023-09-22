#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

response = requests.get('http://0.0.0.0:5050/status')
print('Body response:')
print('\t- type:', type(response.text))
print('\t- content:', response.text)
