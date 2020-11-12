#!/usr/bin/env python3
# coding: utf-8

def decode(text):
    bits = [bin(ord(c))[2:].zfill(8) for c in text]
    out = []

    for i in range(len(bits) // 2):
        ab = bits[2 * i] + bits[2 * i + 1]

        c, d = "", ""
        for i in range(8):
            c += ab[i * 2]
            d = ab[i * 2 + 1] + d

        out += [c, d]

    return ''.join(chr(int(b, 2)) for b in out)
