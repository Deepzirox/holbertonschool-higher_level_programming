#!/usr/bin/python3

""" Ok """

import urllib.request
import sys


def error_code():
    """ error code """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))



if __name__ == '__main__':
    error_code()
