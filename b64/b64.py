#!/usr/bin/env python3

import sys
import base64
import re

"""
Simple Base64 Encoder/Decoder Program for CLI.

Requires: sys, re, and base64 python modules.

Created by Chris Gatewood <chris.gatewood@icg360.com>
"""

__AUTHOR__ = "Chris Gatewood <chris.gatewood@icg360.com>"


def decode(string):
    """ Returns a decoded base64 string"""

    return base64.b64decode(string).decode()


def encode(string):
    """ Returns an encoded base64 string"""

    return base64.b64encode(string.encode()).decode()


def usage():
    """ Prints usage of the program """

    print("""
    Usage:
      b64.py <-d|-e|--decode|--encode|decode|encode> "<string>"

      echo "<somestring>" | b64.py <-d|-e|--decode|--encode|decode|encode>
    """)


def main():
    if len(sys.argv) < 2:
        print("Error: no argument was passed.")
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


if __name__ == "__main__":
    main()
