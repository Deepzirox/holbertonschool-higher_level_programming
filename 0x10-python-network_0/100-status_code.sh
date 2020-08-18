#!/bin/bash
# Make request and print only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
