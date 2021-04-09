#!/usr/bin/env python3

import unittest
from areas import *

class TestAreas(unittest.TestCase):
    def test_triangle(self):
        expected = 5.0
        actual = triangle(2, 5)
        return self.assertEqual(actual, expected)

    def test_rectangle(self):
        expected = 10.0
        actual = rectangle(2, 5)
        return self.assertEqual(actual, expected)

    def test_circle(self):
        expected = 12.566370614359172
        actual = circle(2)
        return self.assertEqual(actual, expected)

unittest.main()
