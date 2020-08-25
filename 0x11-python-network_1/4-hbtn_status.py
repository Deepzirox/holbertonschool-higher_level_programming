#!/usr/bin/python3

""" ok """

import requests


def request_body():
    """ Get status usin requests """
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == '__main__':
    request_body()
