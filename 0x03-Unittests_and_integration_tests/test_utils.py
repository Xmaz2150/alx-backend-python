#!/usr/bin/env python3
"""
"""
import unittest
from utils import *
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    access nested map test class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        valid input
        """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        invalid input
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
