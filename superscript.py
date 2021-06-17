#!/bin/env python

"""
This script does wonder
"""


class Hello:
    """
    Class Hello: a class that prints things
    """

    def __init__(self, *args):
        print(list(sorted(args)))


if __name__ == '__main__':
    for _ in range(10):
        Hello(1, 4, 6, 3, 7, 2)
