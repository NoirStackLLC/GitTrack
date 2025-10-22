#!/usr/bin/env python3
"""
Basic tests for GitTrack functionality.
"""

import unittest
from unittest.mock import Mock, patch
import sys
sys.path.insert(0, '/home/runner/work/GitTrack/GitTrack')
from gittrack import GitTrack


class TestGitTrack(unittest.TestCase):
    """Test cases for GitTrack class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.tracker = GitTrack()
    
    def test_initialization_without_token(self):
        """Test GitTrack initialization without token."""
        tracker = GitTrack()
        self.assertEqual(tracker.base_url, "https://api.github.com")
        self.assertIn("Accept", tracker.headers)
        self.assertIn("User-Agent", tracker.headers)
        self.assertNotIn("Authorization", tracker.headers)
    
    def test_initialization_with_token(self):
        """Test GitTrack initialization with token."""
        token = "test_token"
        tracker = GitTrack(token=token)
        self.assertIn("Authorization", tracker.headers)
        self.assertEqual(tracker.headers["Authorization"], f"token {token}")
    
    @patch('gittrack.requests.get')
    def test_get_repository_info_success(self, mock_get):
        """Test successful repository info retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "full_name": "test/repo",
            "stargazers_count": 100,
            "forks_count": 50
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.tracker.get_repository_info("test", "repo")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["full_name"], "test/repo")
        self.assertEqual(result["stargazers_count"], 100)
        self.assertEqual(result["forks_count"], 50)
    
    @patch('gittrack.requests.get')
    def test_get_repository_info_failure(self, mock_get):
        """Test repository info retrieval failure."""
        import requests
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        
        result = self.tracker.get_repository_info("test", "repo")
        
        self.assertIsNone(result)
    
    @patch('gittrack.requests.get')
    def test_get_commit_count_with_pagination(self, mock_get):
        """Test commit count retrieval with pagination."""
        mock_response = Mock()
        mock_response.json.return_value = [{"sha": "abc123"}]
        mock_response.headers = {
            "Link": '<https://api.github.com/repos/test/repo/commits?page=100>; rel="last"'
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.tracker.get_commit_count("test", "repo")
        
        self.assertEqual(result, 100)
    
    @patch('gittrack.requests.get')
    def test_get_commit_count_without_pagination(self, mock_get):
        """Test commit count retrieval without pagination."""
        mock_response = Mock()
        mock_response.json.return_value = [{"sha": "abc123"}]
        mock_response.headers = {}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.tracker.get_commit_count("test", "repo")
        
        self.assertEqual(result, 1)
    
    @patch('gittrack.requests.get')
    def test_get_issues_count(self, mock_get):
        """Test issues count retrieval."""
        mock_response = Mock()
        mock_response.json.side_effect = [
            {"total_count": 10},  # open issues
            {"total_count": 25}   # closed issues
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        open_issues, closed_issues = self.tracker.get_issues_count("test", "repo")
        
        self.assertEqual(open_issues, 10)
        self.assertEqual(closed_issues, 25)
    
    @patch('gittrack.requests.get')
    def test_get_pull_requests_count(self, mock_get):
        """Test pull requests count retrieval."""
        mock_response = Mock()
        mock_response.json.side_effect = [
            {"total_count": 5},   # open PRs
            {"total_count": 20}   # closed PRs
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        open_prs, closed_prs = self.tracker.get_pull_requests_count("test", "repo")
        
        self.assertEqual(open_prs, 5)
        self.assertEqual(closed_prs, 20)


def run_tests():
    """Run all tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGitTrack)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
