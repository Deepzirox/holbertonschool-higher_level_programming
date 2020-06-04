#!/usr/bin/python3
"""[summary]
"""

from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    new = load_from_json_file('add_item.json')
    new.extend(argv[1:])
    save_to_json_file(new, 'add_item.json')

except FileNotFoundError:
    save_to_json_file(argv[1:], 'add_item.json')