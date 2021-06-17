#!/bin/env python

"""
This script does wonder
"""

class hello:
    def __init__(self, *args):
        # print(**kwargs)
        print(list(sorted(args)))


if __name__ == '__main__':
    for _ in range(10):
        print("oh this one is gonna be a looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong one")
        print("Not Funny","no, really, not funny","I'm telling you, it's not", "really")
        # hello("Not Funny","no, really, not funny","I'm telling you, it's not", "really")
        hello(1,4,6,3,7,2)

