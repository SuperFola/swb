#!/usr/bin/env python3
# coding: utf-8

import sys
from .encode import encode
from .decode import decode


def main(args):
    if args[0] == "-e":
        e = encode(''.join(args[1:]))
        print(e)
        print(decode(e))
    elif args[0] == "-d":
        pass
    else:
        print("""Usage:
    python3 -m swb OPTION text...

OPTION
    -e        Encode the text
    -d        Decode the text

PARAMETERS
    text...   text splitted by a single space between
              each word.
""")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
