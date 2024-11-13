"""
GitHub Repository Visibility Update Script

This script updates the visibility of all private repositories in a GitHub organization to internal.

Usage:
    python update_repo_visibility.py <ORG> <TOKEN>

Arguments:
    ORG   - The GitHub organization name.
    TOKEN - The GitHub token for authentication.

Example:
    python update_repo_visibility.py "QDXEnterpriseOrg" "your_github_token"
"""

import sys
from github import Github
from requests.exceptions import HTTPError

def initialize_github_client(token):
    return Github(token)

def list_repositories(github_client, org):
    repos = []
    for repo in github_client.get_organization(org).get_repos():
        repos.append(repo)
    return repos

def update_repo_visibility(github_client, org):
    repos = list_repositories(github_client, org)
    for repo in repos:
        if repo.private:
            try:
                repo.edit(private=False, visibility='internal')
                print(f"Updated visibility of {repo.name} to internal.")
            except HTTPError as http_err:
                print(f"HTTP error occurred for {repo.name}: {http_err}")
            except Exception as err:
                print(f"Other error occurred for {repo.name}: {err}")

def main(org, token):
    github_client = initialize_github_client(token)
    update_repo_visibility(github_client, org)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_repo_visibility.py <ORG> <TOKEN>")
        sys.exit(1)

    ORG = sys.argv[1]
    TOKEN = sys.argv[2]

    main(ORG, TOKEN)
