#!/usr/bin/env python3
import sys


if __name__ == "__main__":

    if (len(sys.argv) < 2):
        print("[ERROR]")
        print("Usage: pics_parser.py [directory]")
        exit()
    else:
        directory = sys.argv[1]

    print("Now Executing " + sys.argv[0] + "...")
