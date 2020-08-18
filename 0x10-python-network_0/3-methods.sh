#!/bin/bash
# Get allowed methods
curl -sI -XOPTIONS "$1"| grep Allow | cut -d ' ' -f2-
