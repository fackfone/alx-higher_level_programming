#!/usr/bin/python3
"""This python script that takes in an URL
send a request to the URL and finally displays
the body of the response"""
from sys import argv
import requests

if __name__ == "__main__":
    req = requests.post(argv[1])
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
