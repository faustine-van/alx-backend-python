#!/usr/bin/env python3
"""TestAccessNestedMap
   test_utils.py
"""
import requests
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap.test_access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ['a',], 1),
        ({"a": {"b": 2}}, ['a',], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a',]),
        ({"a": 1}, ['a', 'b'])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    estGetJson.test_get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """test_access_nested_map_exception"""
        with patch('utils.requests.get') as mocked_get:
            mock_res = Mock()
            mock_res.json.return_value = expected
            mocked_get.return_value = mock_res

            res = get_json(url)
            mocked_get.assert_called_once_with(url)
            self.assertEqual(res, expected)


class TestMemoize(unittest.TestCase):
    """Test memoize with a specific value for a_method.
        class: - TestMemoize class
    """
    def test_memoize(self):
        """Test class with a_method and a_property.
           method: - test_memoize()
        """

        class TestClass:
            """test class to be memoized.
                   class: TestClass()
            """
            def a_method(self):
                """Method to be memoized.
                   method: a_method()
                """
                return 42

            @memoize
            def a_property(self):
                """Property calling a_method.
                   method: a_property()
                """
                return self.a_method()
        # Mock the a_method using patch and Set return value
        with patch.object(TestClass, 'a_method') as mok:
            instance = TestClass()
            # The first call to a_property
            instance.a_property
            # The second call to a_property
            instance.a_property
            # call once
            mok.assert_called_once()
