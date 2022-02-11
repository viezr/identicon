#!/usr/bin/env python3
from sys import argv, path

path.insert(0, "../app")
from identicon_generator import create_image


def test_save_image(value, size) -> None:
    with open("test_file.png", "bw") as file:
        data = create_image(value, size)
        file.write(data)


if __name__ == "__main__":
    value = argv[1] if len(argv) > 1 else None
    size = argv[2] if len(argv) > 2 else None
    test_save_image(value, size)


