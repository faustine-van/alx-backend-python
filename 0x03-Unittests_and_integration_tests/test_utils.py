#!/usr/bin/env python3
"""TestAccessNestedMap
"""
import requests
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
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
    def test_get_json(self):
        """test_access_nested_map_exception"""
        with patch('utils.requests.get') as mocked_get:
            test_url_1 = 'http://example.com'
            test_url_2 = 'http://holberton.io'
            test_payload = {"payload": True}
            mocked_get.return_value.json.return_value = test_payload
            res = get_json(test_url_1)

            mocked_get.assert_called_once_with(test_url_1)
            self.assertEqual(res, test_payload)

            mocked_get.reset_mock()

            test_payload = {"payload": False}
            mocked_get.return_value.json.return_value = test_payload
            res1 = get_json(test_url_2)

            mocked_get.assert_called_once_with(test_url_2)
            self.assertEqual(res1, test_payload)
