#!/usr/bin/env python3
from sys import path

path.insert(0, "../app")
from identicon_generator import _create_table


def visual_test(end = None):
    def to_char(val):
        return " " if val == 1 else "  "

    strings = ["a", "abc", "vel", "viezr", "Morbi", "tempor", "efficitur",
        "lacus ac", "cursus nulla", "metus consequat"]
    end = end if end < len(strings) else len(strings)

    for st in strings[:end]:
        table = _create_table(st)
        for row in table:
            print(''.join([to_char(x) for x in row]))
        print("\n")

if __name__ == "__main__":
    visual_test(end=4)


