# GitTrack

GitTrack is a simple and effective command-line tool for tracking GitHub repository activity. It displays key information about any public GitHub repository, including stars, forks, commits, issues, and pull requests.

## Features

- 📊 Display repository statistics at a glance
- ⭐ Track star count
- 🍴 Monitor fork count
- 💻 Count total commits
- 📝 Show issues (open and closed)
- 🔀 Display pull requests (open and closed)
- 🚀 Simple command-line interface
- 🔐 Support for GitHub personal access tokens (for higher rate limits)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/NoirStackLLC/GitTrack.git
cd GitTrack
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install requests
```

## Usage

### Basic Usage

Track any public GitHub repository by providing the owner and repository name:

```bash
python gittrack.py owner/repo
```

### Examples

Track the Linux kernel repository:
```bash
python gittrack.py torvalds/linux
```

Track the React repository:
```bash
python gittrack.py facebook/react
```

Track this repository:
```bash
python gittrack.py NoirStackLLC/GitTrack
```

### Using a GitHub Token

For higher rate limits (5000 requests/hour instead of 60), use a GitHub personal access token:

```bash
python gittrack.py owner/repo --token YOUR_GITHUB_TOKEN
```

Or set it as an environment variable:
```bash
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN
python gittrack.py owner/repo
```

### Getting a GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token (classic)
3. Select scopes: `public_repo` (for public repositories)
4. Copy the token and use it with GitTrack

## Output

GitTrack displays the following information:

```
============================================================
GitTrack - Repository Activity Tracker
============================================================

Fetching information for: torvalds/linux
Timestamp: 2025-10-22 01:58:00

Repository: torvalds/linux
Description: Linux kernel source tree
Language: C
Created: 2011-09-04T22:48:12Z
Last Updated: 2025-10-22T01:50:00Z

------------------------------------------------------------

Key Metrics:
  ⭐ Stars:        150,000
  🍴 Forks:        50,000
  👁️  Watchers:     150,000
  
  Fetching commit count...
  💻 Commits:      1,200,000
  Fetching issues count...
  📝 Issues:       500 (Open: 100, Closed: 400)
  Fetching pull requests count...
  🔀 Pull Requests: 1,000 (Open: 50, Closed: 950)

------------------------------------------------------------

Repository URL: https://github.com/torvalds/linux

============================================================
```

## API Rate Limits

GitHub API has rate limits:
- **Unauthenticated requests**: 60 requests per hour
- **Authenticated requests**: 5,000 requests per hour

GitTrack makes multiple API calls to gather all information. Using a token is recommended for tracking multiple repositories.

## Requirements

- Python 3.6 or higher
- `requests` library

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.