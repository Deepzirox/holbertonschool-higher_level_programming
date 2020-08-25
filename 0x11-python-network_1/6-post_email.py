#!/usr/bin/python3


""" Ok """

import requests
import sys


def post_email():
	res = requests.post(argv[1], data={'email': argv[2]})
	print(res.text)



if __name__ == '__main__':
	post_email()
