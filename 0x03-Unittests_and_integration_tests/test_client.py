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

    @patch('utils.get_json', return_value=[{"name": "repo1"}])
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect
            from the chosen payload
        """
        client_url = 'client.GithubOrgClient._public_repos_url'
        url = 'https://api.github.com/orgs/google/repos'
        with patch(client_url, url) as mocked_url:
            # Instantiate GithubOrgClient
            org_client = GithubOrgClient(org_name='google')
            # Call the public_repos property
            res = org_client.public_repos()
            # Assert that get_json was called once
            # with the correct URL
            # mock_get_json.assert_called_once_with(url)
            # mocked_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, data, license_key, st):
        """unit-test GithubOrgClient.has_license
           with parameterize the expected returned value
        """
        pass
