#!/usr/bin/python3
"""This python script takes in a URL, send a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response"""

if __name__ == "__main__":
    import urllib.request
    import sys
    req = sys.argv[1]
    with urllib.request.urlopen(req) as resp:
        print(resp.info()['X-Request-Id'])
        print(resp.info())
