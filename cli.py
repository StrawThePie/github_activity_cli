import argparse
from rich.table import Table
from rich.console import Console
from github_api import fetch_user_events

def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity CLI")
    parser.add_argument("username", help="GitHub username to fetch public events for")
    parser.add_argument(
        "--page",
        type=int,
        default=1,
        help="Page number of results to fetch (default: 1)"
    )
    args = parser.parse_args()

    events = fetch_user_events(args.username, page=args.page)
    if not events:
        print("No events found or user does not exist.")
        return

    console = Console()
    table = Table(title=f"Recent Public Events for {args.username} (Page {args.page})")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Repo", style="magenta")
    table.add_column("Date", style="green")

    for event in events:
        event_type = event.get("type", "")
        repo = event.get("repo", {}).get("name", "")
        created_at = event.get("created_at", "")
        table.add_row(event_type, repo, created_at)

    console.print(table)

if __name__ == "__main__":
    main()
