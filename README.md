# GitHub User Activity CLI

A simple command-line tool written in Python that shows a GitHub user's recent public activity (commits, issues, pull requests, and more) in your terminal. The tool talks to the GitHub REST API, formats the response, and prints it in a readable table, making it a practical example of working with APIs and CLIs.

Created for https://roadmap.sh/projects/github-user-activity

## Features

- Fetch recent public events for any GitHub username (including your own).
- Nicely formatted terminal output using the `rich` library (table with event type, repository, and timestamp).
- Pagination support via a `--page` argument so you can browse older events.
- Configuration via `.env` file so your GitHub Personal Access Token never appears in the code.
- Basic error handling for:
  - Missing or invalid token
  - Invalid usernames
  - Network or HTTP errors (non-200 responses)

## Tech Stack

- Python
- `requests` for HTTP calls to the GitHub API
- `rich` for pretty terminal output
- `python-dotenv` for loading environment variables from `.env`
- `argparse` for command-line arguments (username and page)

## Project Structure

```text
github_activity_cli/
│
├── cli.py            # Main entry point: parses args and prints tables
├── github_api.py     # Functions for calling the GitHub API and handling pagination
├── utils.py          # Helper functions (room for future utilities)
├── .env              # Holds GITHUB_TOKEN (not committed)
├── .gitignore        # Ignores .env, .venv, __pycache__, etc.
└── README.md         # Project documentation

```
## Setup and Instillation

1. Clone the repository
```text
git clone https://github.com/<your-username>/github_activity_cli.git
cd github_activity_cli
```
2. Create and activate a virtual environment
```text
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```
3. Install dependencies
```text
pip install requests rich python-dotenv pytest
```

4. Configure your GitHub token

- Create a Personal Access Token in your GitHub account settings with at least the ```read:user``` scope (and optionally ```repo``` if you later want private activity).
- In the project root, create a file named ```.env```:
```text
GITHUB_TOKEN=your_token_here
```

- Make sure ```.env``` is listed in ```.gitignore``` so it is not committed.

## Usage

From and activated virtual environment in the project root:

- Show first page of your own activity
``` text
python cli.py StrawThePie
```
- Show a specific page of activity
```text
python cli.py StrawThePie --page 2
```

- Look up another user
```text
python cli.py octocat
```
- Example output
```text
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type                 ┃ Repo                          ┃ Date                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ PushEvent            │ StrawThePie/github_activity   │ 2026-01-04T21:32:10Z │
│ IssuesEvent          │ StrawThePie/another-repo      │ 2026-01-03T15:04:55Z │
│ PullRequestEvent     │ StrawThePie/project-x         │ 2026-01-02T10:11:42Z │
└──────────────────────┴───────────────────────────────┴──────────────────────┘
```

## Testing and Code Quality

The project is structured so that API logic in ```github_api.py``` can be tested separately from the CLI in ```cli.py```. You can add tests with ```pytest``` to:

- Mock GitHub API responses
- Check behavior for invalid usernames
- Check responses when the API rate limit or network errors occur

Run tests (once added):

```text
pytest
```

Author StrawThePie