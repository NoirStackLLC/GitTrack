# GitTrack

A Python script for tracking GitHub repository activity including stars, forks, commits, issues, pull requests, and contributors.

## Features

- Track repository statistics (stars, forks, open issues, watchers)
- View recent commits
- List open issues
- List open pull requests
- View contributors and their contribution counts

## Installation

1. Clone this repository:
```bash
git clone https://github.com/NoirStackLLC/GitTrack.git
cd GitTrack
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to configure your GitHub credentials:

1. Generate a GitHub Personal Access Token:
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Click "Generate new token"
   - Select appropriate scopes (at minimum, `repo` for private repositories or `public_repo` for public repositories)
   - Copy the generated token

2. Edit `github_tracker.py` and replace the placeholder values:
   - `token`: Replace `'your_personal_access_token'` with your GitHub Personal Access Token
   - `username`: Replace `'your_github_username'` with the repository owner's username
   - `repo_name`: Replace `'your_repository_name'` with the repository name you want to track

## Usage

Run the script:
```bash
python github_tracker.py
```

The script will display:
- Repository statistics
- Latest 5 commits
- Open issues
- Open pull requests
- Contributors list

## Example Output

```
Repository: username/repository_name
Stars: 100
Forks: 25
Open Issues: 5
Watchers: 50

Recent Commits:
- John Doe: Update README.md on 2024-01-15 10:30:00
- Jane Smith: Fix bug in main function on 2024-01-14 15:20:00
...

Open Issues:
- Bug in feature X (Opened by user1)
- Feature request: Add Y (Opened by user2)
...

Open Pull Requests:
- Fix for issue #123 (Created by contributor1)
...

Contributors:
- contributor1 (Contributions: 50)
- contributor2 (Contributions: 30)
...
```

## Requirements

- Python 3.6+
- PyGithub

## License

This project is open source and available under the MIT License.