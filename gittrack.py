#!/usr/bin/env python3
"""
GitTrack - GitHub Repository Activity Tracker

Track activity in GitHub repositories and display key information such as:
- Number of stars
- Number of forks
- Number of commits
- Number of issues
- Number of pull requests
"""

import argparse
import sys
import requests
from datetime import datetime


class GitTrack:
    """Main class for tracking GitHub repository activity."""
    
    def __init__(self, token=None):
        """
        Initialize GitTrack with optional GitHub token.
        
        Args:
            token: GitHub personal access token for authenticated requests
        """
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitTrack-CLI"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def get_repository_info(self, owner, repo):
        """
        Fetch repository information from GitHub API.
        
        Args:
            owner: Repository owner (username or organization)
            repo: Repository name
            
        Returns:
            dict: Repository information or None if error
        """
        url = f"{self.base_url}/repos/{owner}/{repo}"
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 403:
                print(f"Error: API rate limit exceeded or access forbidden.", file=sys.stderr)
                print(f"Tip: Use a GitHub token with --token flag for higher rate limits.", file=sys.stderr)
            else:
                print(f"Error fetching repository info: {e}", file=sys.stderr)
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repository info: {e}", file=sys.stderr)
            return None
    
    def get_commit_count(self, owner, repo):
        """
        Get the total number of commits in the repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            int: Number of commits or 0 if error
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        try:
            # Get the first page to check the Link header
            response = requests.get(url, headers=self.headers, params={"per_page": 1}, timeout=30)
            response.raise_for_status()
            
            # Check if there's pagination info in the Link header
            link_header = response.headers.get("Link", "")
            if "last" in link_header:
                # Extract the last page number from the Link header
                import re
                match = re.search(r'page=(\d+)>; rel="last"', link_header)
                if match:
                    return int(match.group(1))
            
            # If no pagination, count the commits on this page
            commits = response.json()
            return len(commits) if commits else 0
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch commit count: {e}", file=sys.stderr)
            return 0
    
    def get_issues_count(self, owner, repo):
        """
        Get the count of open and closed issues (excluding pull requests).
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            tuple: (open_issues, closed_issues)
        """
        try:
            # Get open issues count
            url = f"{self.base_url}/search/issues"
            params = {
                "q": f"repo:{owner}/{repo} type:issue state:open",
                "per_page": 1
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            open_issues = response.json().get("total_count", 0)
            
            # Get closed issues count
            params["q"] = f"repo:{owner}/{repo} type:issue state:closed"
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            closed_issues = response.json().get("total_count", 0)
            
            return open_issues, closed_issues
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch issues count: {e}", file=sys.stderr)
            return 0, 0
    
    def get_pull_requests_count(self, owner, repo):
        """
        Get the count of open and closed pull requests.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            tuple: (open_prs, closed_prs)
        """
        try:
            # Get open PRs count
            url = f"{self.base_url}/search/issues"
            params = {
                "q": f"repo:{owner}/{repo} type:pr state:open",
                "per_page": 1
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            open_prs = response.json().get("total_count", 0)
            
            # Get closed PRs count (includes merged)
            params["q"] = f"repo:{owner}/{repo} type:pr state:closed"
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            closed_prs = response.json().get("total_count", 0)
            
            return open_prs, closed_prs
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch pull requests count: {e}", file=sys.stderr)
            return 0, 0
    
    def track_repository(self, owner, repo):
        """
        Track and display all activity information for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
        """
        print(f"\n{'='*60}")
        print(f"GitTrack - Repository Activity Tracker")
        print(f"{'='*60}\n")
        
        print(f"Fetching information for: {owner}/{repo}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Get basic repository info
        repo_info = self.get_repository_info(owner, repo)
        if not repo_info:
            print("Failed to fetch repository information.")
            return
        
        # Display basic info
        print(f"Repository: {repo_info.get('full_name', 'N/A')}")
        print(f"Description: {repo_info.get('description', 'No description')}")
        print(f"Language: {repo_info.get('language', 'N/A')}")
        print(f"Created: {repo_info.get('created_at', 'N/A')}")
        print(f"Last Updated: {repo_info.get('updated_at', 'N/A')}")
        print(f"\n{'-'*60}\n")
        
        # Display key metrics
        print("Key Metrics:")
        print(f"  ⭐ Stars:        {repo_info.get('stargazers_count', 0):,}")
        print(f"  🍴 Forks:        {repo_info.get('forks_count', 0):,}")
        print(f"  👁️  Watchers:     {repo_info.get('watchers_count', 0):,}")
        
        # Get and display commit count
        print("\n  Fetching commit count...")
        commit_count = self.get_commit_count(owner, repo)
        print(f"  💻 Commits:      {commit_count:,}")
        
        # Get and display issues count
        print("  Fetching issues count...")
        open_issues, closed_issues = self.get_issues_count(owner, repo)
        total_issues = open_issues + closed_issues
        print(f"  📝 Issues:       {total_issues:,} (Open: {open_issues:,}, Closed: {closed_issues:,})")
        
        # Get and display pull requests count
        print("  Fetching pull requests count...")
        open_prs, closed_prs = self.get_pull_requests_count(owner, repo)
        total_prs = open_prs + closed_prs
        print(f"  🔀 Pull Requests: {total_prs:,} (Open: {open_prs:,}, Closed: {closed_prs:,})")
        
        print(f"\n{'-'*60}\n")
        print(f"Repository URL: {repo_info.get('html_url', 'N/A')}")
        print(f"\n{'='*60}\n")


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="GitTrack - Track GitHub repository activity and display key metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  gittrack.py owner/repo
  gittrack.py torvalds/linux
  gittrack.py facebook/react --token YOUR_GITHUB_TOKEN
  
Environment Variables:
  GITHUB_TOKEN - GitHub personal access token for authenticated requests
        """
    )
    
    parser.add_argument(
        "repository",
        help="Repository in format 'owner/repo' (e.g., 'torvalds/linux')"
    )
    
    parser.add_argument(
        "-t", "--token",
        help="GitHub personal access token (optional, for higher rate limits)",
        default=None
    )
    
    args = parser.parse_args()
    
    # Parse repository
    if "/" not in args.repository:
        print("Error: Repository must be in format 'owner/repo'", file=sys.stderr)
        sys.exit(1)
    
    owner, repo = args.repository.split("/", 1)
    
    # Check for token in environment if not provided
    import os
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    # Create GitTrack instance and track repository
    tracker = GitTrack(token=token)
    tracker.track_repository(owner, repo)


if __name__ == "__main__":
    main()
