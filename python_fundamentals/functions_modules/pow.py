#!/usr/bin/env python3


def pow(a, b):
    result = 1
    exponent = b

    if b < 0:
        exponent = -b

    while exponent > 0:
        result *= a
        exponent -= 1

    if b < 0:
        return 1 / result

    return result
