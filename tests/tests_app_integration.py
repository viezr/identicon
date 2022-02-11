#!/usr/bin/env python3
'''
Ident icon generator. Web app tests.
'''
import unittest
import urllib.request


class IdentIconTests(unittest.TestCase):
    '''
    Test identicon web app.
    '''
    def test_homepage_returnText(self):
        expected = "Icon image generator"
        with urllib.request.urlopen("http://localhost:5000/") as page:
            resp = page.read(100).decode('utf-8')
        self.assertIn(expected, resp)

    def test_getImage_returnResponseImageType(self):
        with urllib.request.urlopen("http://localhost:5000/getimage/a") as page:
            resp = page.headers["content-type"]
        self.assertEqual(resp, "image/png")

    def test_getImage_returnResponseBytes(self):
        with urllib.request.urlopen("http://localhost:5000/getimage/a") as page:
            resp = page.read(100)
        self.assertIsInstance(resp, bytes)

    def test_getImage_returnPNGimage(self):
        with urllib.request.urlopen("http://localhost:5000/getimage/a") as page:
            resp = page.read()[:5]
        self.assertIn(b"\x89PNG", resp)

if __name__ == "__main__":
    unittest.main(warnings="ignore")
