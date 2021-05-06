"""
One Time Password Key Generation
"""

from random import choice , randint

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def genkey():
    s = ""
    for _ in range(randint(6, 8)):
        s += choice(chars)
    return s
