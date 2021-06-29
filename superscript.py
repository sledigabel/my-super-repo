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
        """
        do_nothing does nothing
        """


if __name__ == '__main__':
    for _ in range(10):
        h = Hello(1, 3, 6, 3, 7, 2)

        # asd;fkljasdkl;rfjasl;djf;lasjdfl;kjsadl;kfjasdl;kjfl;askdjf;lkasdjfl;kasjdl;fjasl
        h.do_print()
