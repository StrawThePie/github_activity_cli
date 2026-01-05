GitHub User Activity CLI
A polished Python command-line tool that fetches and displays a GitHub user’s recent public activity (commits, issues, pull requests, and more) directly in the terminal. This project was built as a learning-focused implementation of the GitHub User Activity challenge from roadmap.sh, with extra features like rich formatting, pagination, and robust error handling.

Highlights
Tech stack: Python, requests, rich, python-dotenv, argparse.

Fetches recent public events for any GitHub user and renders them in a clean, colorized table in the terminal.

Built to practice real-world skills: working with REST APIs, handling JSON, building CLIs, and managing configuration securely.

Shows experience with:

Python and virtual environments.

API authentication (GitHub Personal Access Tokens) and .env-based configuration.

Modular code organization and git/GitHub version control.

What It Does
Accepts a GitHub username (and optional page number) as CLI arguments.

Authenticates with the GitHub API using a Personal Access Token stored in a .env file.

Fetches the user’s public events from https://api.github.com/users/<username>/events.

Displays events in a Rich table with:

Event type (for example, PushEvent, IssuesEvent, PullRequestEvent)

Repository name

Timestamp.

Supports pagination so you can explore older activity with --page.

Handles invalid users, missing tokens, network issues, and non-200 responses with clear messages.

Project Structure
text
github_activity_cli/
├── cli.py          # CLI entrypoint (argparse, Rich table rendering)
├── github_api.py   # GitHub API client (requests, auth, pagination, error handling)
├── utils.py        # Helpers and future utility functions
├── .env            # Local secrets (GITHUB_TOKEN), ignored by git
├── .gitignore      # Ignores .env, .venv, __pycache__, etc.
├── README.md       # Project documentation
cli.py focuses on user experience: parsing arguments, formatting output, and keeping the interface intuitive.

github_api.py handles API details: building URLs, sending requests, handling pagination, and returning usable data to the CLI.

Setup and Installation
1. Clone the Repository
bash
git clone https://github.com/<your-username>/github_activity_cli.git
cd github_activity_cli
2. Create and Activate a Virtual Environment
bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
3. Install Dependencies
bash
pip install requests rich python-dotenv pytest
4. Configure Your GitHub Token
Generate a Personal Access Token in your GitHub account settings.

Grant minimal scopes such as read:user (and optionally repo if you later want private activity).

Create a .env file in the project root:

text
GITHUB_TOKEN=your_token_here
.env should be listed in .gitignore so the token is not committed.

Usage
From an activated virtual environment:

Basic: First Page of Events
bash
python cli.py StrawThePie
Paginated: Second Page of Events
bash
python cli.py StrawThePie --page 2
Different User
bash
python cli.py octocat
Example terminal output:

text
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type                 ┃ Repo                          ┃ Date                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ PushEvent            │ StrawThePie/github_activity   │ 2026-01-04T21:32:10Z │
│ IssuesEvent          │ StrawThePie/another-repo      │ 2026-01-03T15:04:55Z │
│ PullRequestEvent     │ StrawThePie/project-x         │ 2026-01-02T10:11:42Z │
└──────────────────────┴───────────────────────────────┴──────────────────────┘
Testing and Code Quality
Designed with testing in mind using pytest.

Separation of cli.py and github_api.py allows testing API logic independently from the CLI layer.

Future tests can:

Mock GitHub API responses.

Validate behavior for invalid usernames, rate-limited responses, and timeouts.

Run tests (when added):

bash
pytest
Learning Outcomes
This project demonstrates:

API integration: authenticated GET requests against the GitHub REST API, including headers, timeouts, and HTTP error handling.

JSON parsing: working with nested event payloads and extracting meaningful fields.

CLI design: building a user-friendly interface with argparse and rich terminal output.

Configuration management: using .env and python-dotenv to keep secrets out of source control.

Version control discipline: structuring a project with git and GitHub from the beginning.

Future Work
Possible enhancements:

Filter by event type (for example, only pushes or only issues).

Add flags for compact versus detailed views.

Export activity to JSON or CSV for analysis.

Integrate GitHub’s GraphQL API for richer queries and more efficient data fetching.

Package the tool as a pip-installable CLI with an entry point script.

About the Project
This CLI is part of a broader effort to build practical, API-driven Python tools based on roadmap-style projects, with a focus on clean code, good developer experience, and real-world patterns.