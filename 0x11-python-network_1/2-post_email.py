#!/usr/bin/python3
"""This python script takes in a URL, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response decoded in utf-8"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse
    email = argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode()
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
