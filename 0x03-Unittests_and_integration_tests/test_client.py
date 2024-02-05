#!/usr/bin/env python3
"""TestAccessNestedMap
   test_utils.py
"""
import unittest
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch, PropertyMock
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

        # Assert that the mock_get_json was called once
        # with the expected argument
        url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(url)

        # Assert that the result is the mocked response
        self.assertEqual(result, f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """ Mock property Test that the result of _public_repos_url
            is the expected one based on the mocked payload.
        """
        client_org = 'client.GithubOrgClient.org'
        with patch(client_org, new_callable=PropertyMock()) as mock:
            GithubOrgClient._public_repos_url

    @patch('utils.get_json', new_callable=PropertyMock())
    def test_public_repos(self, mock):
        """Test that the list of repos is what you expect
            from the chosen payload
        """

        mock.return_value = 'Success'
        GithubOrgClient.public_repos
        client_url = 'client.GithubOrgClient._public_repos_url'
        with patch(client_url, new_callable=PropertyMock()) as mocked_pro:
            mocked_pro.return_value = 'Real Url'
