#!/usr/bin/python3

import sys, requests


def error_code():
	if requests.get(argv[1]).status_code > 400:
		re = requests.get(argv[1])
		print("Error code: {}".format(re.status_code))
	else:
		print(re.text)


if __name__ == '__main__':
	error_code()
