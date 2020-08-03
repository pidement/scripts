#!/bin/python3
# https://en.wikipedia.org/wiki/Base64

import argparse
import base64

parser = argparse.ArgumentParser(description='encode string in base64')
parser.add_argument('code', metavar='CODE', type=str, help='code')

args = parser.parse_args()

base64_message = args.code
base64_bytes = base64_message.encode('utf-8')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('utf-8')

print(message)
