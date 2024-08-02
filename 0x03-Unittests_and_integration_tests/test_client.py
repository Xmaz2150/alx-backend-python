#!/usr/bin/env python3
"""
test obj mudule
"""
import unittest
import mock
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    GithubOrgClient test class
    """
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org, url, mock_get_json):
        """
        test org method
        """
        obj = GithubOrgClient(org)
        obj.org

        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """
        patch GithubOrgClient.org
        """
        with patch(
                    'client.GithubOrgClient.org',
                    new_callable=mock.PropertyMock
                ) as mock_property:
            mock_property.return_value = {
                    'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            res = GithubOrgClient('google')._public_repos_url
            self.assertEqual(res, 'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        """
        with patch(
                    'client.GithubOrgClient._public_repos_url',
                    new_callable=mock.PropertyMock
                ) as mock_property:
            mock_property.return_value = {
                    'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            res = GithubOrgClient('google')._public_repos_url
            self.assertEqual(res['repos_url'], 'https://api.github.com/orgs/google/repos')


    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        GithubOrgClient.has_license test case
        """
        res = GithubOrgClient('google').has_license(repo, license_key)
        self.assertEqual(res, expected)
