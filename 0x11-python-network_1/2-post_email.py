#!/usr/bin/python3

""" Ok """

from urllib import request, parse
import sys


def post_email():
    """ Post email to given url """
    url = sys.argv[1]
    value = sys.argv[2]
    data = {"email": value}
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf8"))


if __name__ == '__main__':
    post_email()
