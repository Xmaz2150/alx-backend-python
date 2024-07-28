#!/usr/bin/env python3
"""
"""
import unittest
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """
    get jason test class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """
        mocks `get json`
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get_json.return_value = mock_response

        res = get_json(test_url)

        mock_get_json.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """
    memoize test class
    """
    def test_memoize(self):
        """
        mocks a method decorated by `memoize`
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_a_method:
            """
            alternative to patch decoration on `test_memoize`
            """
            test = TestClass()

            res1 = test.a_property
            res2 = test.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
