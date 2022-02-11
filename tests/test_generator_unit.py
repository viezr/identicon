#!/usr/bin/env python3
import unittest
from random import choice
from sys import path

path.insert(0, "../app")
from identicon_generator import _parse_input
from identicon_generator import _create_table, _create_pixmap, create_image


class IdentIconGeneratorTests(unittest.TestCase):
    '''
    Test IdentIcon generator.
    '''
    def setUp(self):
        self._default_value = "abc"
        self._default_size = 80
        self._default_size_range = (5, 256)

    def test_createTable_return5rows(self):
        result = _create_table(self._default_value)
        rows = len(result)
        self.assertEqual(5, rows)

    def test_createTable_return5columns(self):
        result = _create_table(self._default_value)
        five_columns = all((len(x) == 5 for x in result))
        self.assertTrue(five_columns)

    def test_parseInputValueNonStr_returnDefaultStr(self):
        result = _parse_input(None, 60)[0]
        self.assertEqual(result, self._default_value)

    def test_parseInputValue_returnValue(self):
        result = _parse_input("test", 60)[0]
        self.assertEqual(result, "test")

    def test_parseInputSizeNone_returnDefault(self):
        result = _parse_input(None, None)[1]
        self.assertEqual(result, self._default_size)

    def test_parseInputSizeAsStr_returnIntSize(self):
        result = _parse_input(None, "95")[1]
        self.assertEqual(result, 95)

    def test_parseInputSize_returnSize(self):
        result = _parse_input(None, 95)[1]
        self.assertEqual(result, 95)

    def test_parseInputSizeNotInRange_returnDefault(self):
        outrange_sizes = list(range(-100, self._default_size_range[0]))
        outrange_sizes += list(range(self._default_size_range[1], 1000))
        rand_out_size = choice(outrange_sizes)
        result = _parse_input(None, rand_out_size)[1]
        self.assertEqual(result, self._default_size)

    def test_createPixmap_returnList(self):
        result = _create_pixmap("test")
        self.assertIsInstance(result, list)

    def test_createImage_returnBytes(self):
        result = create_image()
        self.assertIsInstance(result, bytes)

    def test_createImage_returnPNGimage(self):
        result = create_image()[:5]
        self.assertIn(b"\x89PNG", result)


if __name__ == "__main__":
    unittest.main(warnings="ignore")


