#!/bin/bash
# SEND DELETE REQUEST
RES=$(curl -s -XDELETE "$1") && printf %s "$RES"
