#!/usr/bin/python3

""" Ok """

import requests
from sys import argv


def commit():
    """ Ok """
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    re = req.json()[:10]
    for c in re:
        sha = c.get('sha')
        commit = c.get('commit')
        author = commit.get('author')
        name = author.get('name')
        print("{}: {}".format(sha, name))


if __name__ == "__main__":
    commit()
