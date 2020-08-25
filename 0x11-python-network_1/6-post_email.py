#!/usr/bin/python3


""" Ok """

import requests, sys


def post_email():
	url = sys.argv[1]
	email = sys.argv[2]
	val = {"email": email}
	res = requests.post(url, data=val)
	print(res.text)



if __name__ == '__main__':
	post_email()
