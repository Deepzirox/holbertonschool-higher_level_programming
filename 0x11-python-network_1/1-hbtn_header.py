#!/usr/bin/python3

""" OK """

import urllib.request
import sys


def get_request_id():
    """ GET REQUEST ID FROM HEADER """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        headers = res.headers
        print(headers.get("X-Request-Id"))


if __name__ == '__main__':
    get_request_id()
