#!/usr/bin/env python3
'''
Ident icon tests.
'''
import unittest

from identicon import app, main_route


class IdentIconTests(unittest.TestCase):
    '''
    Test identicon web app.
    '''
    def test_appinit_returnTrue(self):
        self.assertTrue(app)

    def test_mainRoute_returnResponseImageType(self):
        resp = main_route("test_name")
        self.assertEqual(resp.content_type, "image/png")

    def test_mainRoute_returnResponseImageData(self):
        resp = main_route("test_name")
        self.assertIsInstance(resp.response[0], bytes)

if __name__ == "__main__":
    unittest.main(warnings="ignore")
