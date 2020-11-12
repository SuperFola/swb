#!/usr/bin/env python3
# coding: utf-8


def encode(text, bit_swap=1):
    bits = list(bin(ord(c))[2:].zfill(8) for c in text)
    if len(bits) % 2 == 1:
        bits.append(''.zfill(8))
    out = []

    for i in range(len(bits) // 2):
        a, b = bits[2 * i], bits[2 * i + 1]

        c, d = "", ""
        for i in range(4):
            c += a[i]     + b[7 - i]
            d += a[4 + i] + b[3 - i]

        out += [c, d]

    return ''.join(chr(int(b, 2)) for b in out)
