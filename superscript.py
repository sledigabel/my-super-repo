#!/bin/env python

"""
This script does wonder
"""


class Hello:
    """
    Class Hello: a class that prints things
    """

    def __init__(self, *args):
        self.args = args

    def do_print(self):
        """
        do_print does the printing
        """
        print(list(sorted(self.args)))

    def do_nothing(self):
        pass


if __name__ == '__main__':
    for _ in range(10):
        h = Hello(1, 4, 6, 3, 7, 2)
        h.do_print()
