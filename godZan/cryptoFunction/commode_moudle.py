# coding=utf-8
import sys
sys.setrecursionlimit(10000000)
"""
选择相同的模 n 加密相同的信息 m
"""

helpstr = '''
usage:
    c1 = m ^ e1 % n
    c2 = m ^ e2 % n
'''


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m