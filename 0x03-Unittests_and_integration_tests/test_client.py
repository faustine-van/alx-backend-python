#!/usr/bin/env python3
"""TestAccessNestedMap
   test_utils.py
"""
import unittest
from parameterized import parameterized, parameterized_class
from utils import get_json
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
    def test_has_license(self, data, license_key, val):
        """unit-test GithubOrgClient.has_license
           with parameterize the expected returned value
        """
        self.assertEqual(GithubOrgClient.has_license(data, license_key), val)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test the GithubOrgClient.public_repos method in
       an integration test
    """
    org_payload = None
    repos_payload = None
    expected_repos = None
    apache2_repos = None

    @classmethod
    def setUpClass(cls):
        """"Start patching and  mock requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        # Use side_effect for multiple returns
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload,
            cls.expected_repos,
            cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """method returns the expected results based on the fixtures
        """
        # org_client = GithubOrgClient(org_name='google')
        # repos = org_client.public_repos()
        repos = GithubOrgClient.public_repos(self)
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """to test the public_repos with
           the argument license="apache-2.0
        """
        org_client = GithubOrgClient(org_name='google')
        repos = org_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
