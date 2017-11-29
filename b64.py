#!/usr/bin/python

import sys
import base64
import re

'''
Simple Base64 Encoder/Decoder Program for CLI.

Requires: sys, re, and base64 python modules.

Created by Chris Gatewood <chris.gatewood@icg360.com>
'''

__AUTHOR__ = "Chris Gatewood <chris.gatewood@icg360.com>"


# Decode function
def decode(string):
    return base64.b64decode(string).decode()


# Encode function
def encode(string):
    return base64.b64encode(string.encode()).decode()


# Print usage of the program (probably needs fleshing out since it can do
# both piping and standard params)
def usage():
    print('Usage: b64.py -d|-e|--decode|--encode|decode|encode "<string>"')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    # Break down the choice to 'e' or 'd' regardless of which form used, 'e'
    # and 'd' could also be specified on CLI
    choice = re.sub("-|ncode|ecode", "", sys.argv[1], flags=re.I)

    # Check if string parameter is piped in using "echo" or something else, if
    # nothing specified, quit with usage
    if not sys.stdin.isatty():
        param = sys.stdin.readline()
    elif len(sys.argv) == 3:
        param = sys.argv[2]
    else:
        usage()
        sys.exit(1)

    # Meat and potatoes!
    if choice == 'e':
        print(encode(param))
    elif choice == 'd':
        print(decode(param))
    else:
        usage()
        sys.exit(1)
