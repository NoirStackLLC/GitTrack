# GitTrack

## Description
A Python-based GitHub activity tracker that monitors repository statistics such as stars, forks, commits, issues, pull requests, and contributors. Built with the **Noir Stack** for efficient, lightweight tracking of GitHub activity.

## About
This repository provides a simple Python script to track various GitHub repository activities. By using the GitHub API, it allows you to easily fetch data like:
- **Stars**: How many users have starred your repository.
- **Forks**: How many users have forked your repository.
- **Commits**: A list of recent commits and their messages.
- **Issues and Pull Requests**: Information about open issues and pull requests.
- **Contributors**: A list of contributors to the repository.

Built with the **Noir Stack**, a technology stack that emphasizes performance, simplicity, and scalability, this tracker is optimized for handling various GitHub activity monitoring use cases efficiently. 

This tool is useful for repository owners and contributors who want to analyze their GitHub activity and track their project's growth over time.

## Features
- Monitor stars, forks, and watchers.
- Track recent commits and their authors.
- Get details on open issues and pull requests.
- Track contributors and their contributions to the repository.
- Easy-to-use Python script using the PyGitHub library.

## Requirements
- Python 3.x
- `PyGitHub` library

To install the required Python library, run:
pip install PyGithub

## Setup

1. Clone the repository:
git clone https://github.com/your_username/your_repository_name.git
cd your_repository_name

2. Create a GitHub Personal Access Token:
- Go to [GitHub's Personal Access Tokens](https://github.com/settings/tokens) and generate a new token with the `repo`, `public_repo`, and `read:user` scopes.

3. Edit the Python script to include your **GitHub username** and **Personal Access Token**.

4. Run the script:
python github_tracker.py

## Example Output
After running the script, you should see output similar to the following:

Repository: your_github_username/your_repository_name

Stars: 45
Forks: 12
Open Issues: 3
Watchers: 8

Recent Commits:

John Doe: Added feature X on 2025-10-22 10:23:45
Jane Smith: Fixed bug Y on 2025-10-21 15:10:30

Open Issues:

Issue #1: Bug in feature X (Opened by john_doe)
Issue #2: Feature Y request (Opened by jane_smith)

Contributors:

john_doe (Contributions: 10)
jane_smith (Contributions: 5)


## Contributing
Feel free to fork the repository and create pull requests with any improvements or bug fixes. If you have any questions or suggestions, open an issue, and we'll be happy to help.

## License
This project is open-source and available under the MIT License. The **Noir Stack** components used in this project are lightweight and designed to optimize performance, making this GitHub Activity Tracker efficient for real-time monitoring.

The license allows you to freely use, modify, and distribute the code as long as you adhere to the terms of the MIT License.

## About Noir Stack
The **Noir Stack** refers to a set of technologies optimized for building scalable, efficient applications. For this project, it combines lightweight Python libraries with the GitHub API to track and display activity without unnecessary overhead. The stack emphasizes simplicity, performance, and ease of use, making it ideal for building data-tracking tools like this GitHub Activity Tracker.

## License Summary
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.

