from github import Github

# Replace with your GitHub Personal Access Token
token = 'your_personal_access_token'

# Authenticate with GitHub
g = Github(token)

# Replace with your GitHub username and the repository name you want to track
username = 'your_github_username'
repo_name = 'your_repository_name'

# Get the repository
repo = g.get_repo(f"{username}/{repo_name}")

# Track repository activity
print(f"Repository: {repo.full_name}")
print(f"Stars: {repo.stargazers_count}")
print(f"Forks: {repo.forks_count}")
print(f"Open Issues: {repo.open_issues_count}")
print(f"Watchers: {repo.subscribers_count}")

# Get recent commits
print("\nRecent Commits:")
commits = repo.get_commits()
for commit in commits[:5]:  # Show the latest 5 commits
    print(f"- {commit.committer.name}: {commit.commit.message} on {commit.committer.date}")

# Get open issues
print("\nOpen Issues:")
issues = repo.get_issues(state="open")
for issue in issues:
    print(f"- {issue.title} (Opened by {issue.user.login})")

# Get open pull requests
print("\nOpen Pull Requests:")
pulls = repo.get_pulls(state="open")
for pr in pulls:
    print(f"- {pr.title} (Created by {pr.user.login})")

# Get contributors
print("\nContributors:")
contributors = repo.get_contributors()
for contributor in contributors:
    print(f"- {contributor.login} (Contributions: {contributor.contributions})")
