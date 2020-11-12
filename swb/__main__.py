#!/usr/bin/env python3
# coding: utf-8

import sys
from .encode import encode
from .decode import decode


def main(args):
    if len(args) > 0:
        e = encode(''.join(args))
        print(e)
        print(decode(e))
    else:
        print("""Usage:
    python3 -m swb text...

PARAMETERS
    text...   text splitted by a single space between
              each word.
""")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
