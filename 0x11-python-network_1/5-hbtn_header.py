#!/usr/bin/python3

""" ok """

import requests
import sys


def request_body():
    """ Get status usin requests """
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))


if __name__ == '__main__':
    request_body()
