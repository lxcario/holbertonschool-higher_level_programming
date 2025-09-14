#!/usr/bin/python3
""" Unittests for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_max_end(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), 5)

    def test_max_first(self):
        test_list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def test_max_middle(self):
        test_list = [12, 23, 40, 11, 2]
        self.assertEqual(max_integer(test_list), 40)

    def test_max_one_negative(self):
        test_list = [1, 2, -6, 7, 2]
        self.assertEqual(max_integer(test_list), 7)

    def test_max_all_negative(self):
        test_list = [-1, -2, -3, -5, -10]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_max(self):
        test_list = [100]
        self.assertEqual(max_integer(test_list), 100)
