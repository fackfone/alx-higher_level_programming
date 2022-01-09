#!/usr/bin/python3
"""This python script fetches https://intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user')
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
