#!/usr/bin/env python3
"""TestAccessNestedMap
   test_utils.py
"""
import unittest
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test that GithubOrgClient.org returns the correct value.
    """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json', side_effect=lambda url: f'{url}')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        
        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient(org_name)

        # Call the org method
        result = github_org_client.org

        # Assert that the mock_get_json was called once with the expected argument
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

        # Assert that the result is the mocked response
        self.assertEqual(result, f'https://api.github.com/orgs/{org_name}')