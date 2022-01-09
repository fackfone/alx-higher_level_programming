#!/usr/bin/python3
"""This python script takes in a URL, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response decoded in utf-8
This script also handle the URLError and the HTTPError"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import urllib.parse

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
