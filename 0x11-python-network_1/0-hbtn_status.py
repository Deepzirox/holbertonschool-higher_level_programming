#!/usr/bin/python3

""" OK """

import urllib.request

def hbtn_status():
	"""
		Get Body response
	"""
	url = "https://intranet.hbtn.io/status"
	with urllib.request.urlopen(url) as response:
		res = response.read()
		print("Body response:")
		print("\t- type: {}".format(type(res)))
		print("\t- content: {}".format(res))
		print("\t- utf8 content: {}".format(res.decode("utf8")))


if __name__ == '__main__':
	hbtn_status()
