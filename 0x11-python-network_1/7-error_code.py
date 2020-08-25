#!/usr/bin/python3

import sys, requests


def error_code():
	re = requests.get(argv[1])
	if re.status_code > 400:
		
		print("Error code: {}".format(re.status_code))
	else:
		print(re.text)


if __name__ == '__main__':
	error_code()
