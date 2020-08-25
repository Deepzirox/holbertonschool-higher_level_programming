#!/usr/bin/python3

""" ok """

import requests


def request_body():
    """ Get status usin requests """
    req = requests.get("https://intranet.hbtn.io/status")
    print(req.headers["X-Request-Id"])


if __name__ == '__main__':
    request_body()
