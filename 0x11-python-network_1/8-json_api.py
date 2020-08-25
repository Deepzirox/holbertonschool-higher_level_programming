#!/usr/bin/python3

""" Ok """

from sys import argv
import requests


def search():
    """ ok """
    v = argv[1]
    if len(argv) < 2:
        v = ""

    re = requests.post(
        'http://0.0.0.0:5000/search_user', data={'q': v})
    try:
        data = re.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    search()
