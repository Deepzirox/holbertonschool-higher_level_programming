#!/bin/bash
# SEND DATA AND SHOW BODY RESPONSEss
curl -sH "Content-Type: application/json" --data "@$2" "$1"