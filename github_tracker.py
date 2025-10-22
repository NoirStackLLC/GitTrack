import os
from github import Github

# Use environment variable for token for security
token = os.getenv('GITHUB_TOKEN')

if not token:
    print("Error: GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
    exit(1)

# Authenticate with GitHub
g = Github(token)

# Replace with your GitHub username and repository name you want to track
username = 'your_github_username'
repo_name = 'your_repository_name'

# Get the repository
try:
    repo = g.get_repo(f"{username}/{repo_name}")
except Exception as e:
    print(f"Error fetching repository: {e}")
    exit(1)

# Track repository activity
print(f"Repository: {repo.full_name}")
print(f"Stars: {repo.stargazers_count}")
print(f"Forks: {repo.forks_count}")
print(f"Open Issues: {repo.open_issues_count}")
print(f"Watchers: {repo.subscribers_count}")

# Get recent commits
print("\nRecent Commits:")
try:
    commits = repo.get_commits()
    for commit in commits[:5]:  # Show the latest 5 commits
        print(f"- {commit.committer.name}: {commit.commit.message} on {commit.committer.date}")
except Exception as e:
    print(f"Error fetching commits: {e}")

# Get open issues
print("\nOpen Issues:")
try:
    issues = repo.get_issues(state="open")
    for issue in issues:
        print(f"- {issue.title} (Opened by {issue.user.login})")
except Exception as e:
    print(f"Error fetching issues: {e}")

# Get open pull requests
print("\nOpen Pull Requests:")
try:
    pulls = repo.get_pulls(state="open")
    for pr in pulls:
        print(f"- {pr.title} (Created by {pr.user.login})")
except Exception as e:
    print(f"Error fetching pull requests: {e}")

# Get contributors
print("\nContributors:")
try:
    contributors = repo.get_contributors()
    for contributor in contributors:
        print(f"- {contributor.login} (Contributions: {contributor.contributions})")
except Exception as e:
    print(f"Error fetching contributors: {e}")
