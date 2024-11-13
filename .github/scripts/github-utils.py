"""
GitHub Utilities Script

This script provides utility functions for interacting with GitHub and sending email notifications. 
It includes functions to initialize a GitHub client, list repositories in an organization, create or update issues, 
and send email notifications.

Functions:
1. initialize_github_client(token): Initializes and returns a GitHub client using the provided token.
2. list_repositories(github_client, org): Lists all repositories in the specified GitHub organization.
3. create_or_update_issue(github_client, owner, repo, body, issue_title, labels): Creates or updates a GitHub issue with the specified details.
4. send_email_notification(from_address, to_address, smtp_server, smtp_port, subject, body): Sends an email notification with the specified details.

Usage:
    1. Import the script in your main script or workflow.
    2. Use the provided functions to interact with GitHub and send email notifications.

Example:
    from github_utils import initialize_github_client, list_repositories, create_or_update_issue, send_email_notification

    # Initialize GitHub client
    github_client = initialize_github_client("your_github_token")

    # List repositories in an organization
    repos = list_repositories(github_client, "your_org_name")

    # Create or update an issue
    issue_url = create_or_update_issue(github_client, "your_org_name", "your_repo_name", "issue_body", "issue_title", ["label1", "label2"])

    # Send an email notification
    send_email_notification("from@example.com", "to@example.com", "smtp.example.com", 587, "Subject", "Email body")
"""

import requests
from github import Github
from requests.exceptions import HTTPError

# Initialize GitHub client
def initialize_github_client(token):
    return Github(token)

def list_repositories(github_client, org):
    repos = []
    for repo in github_client.get_organization(org).get_repos():
        repos.append(repo.name)
    return repos

def create_or_update_issue(github_client, owner, repo, body, issue_title, labels):
    repo = github_client.get_repo(f"{owner}/{repo}")
    issues = repo.get_issues(state="open", labels=labels)
    issue = None
    for i in issues:
        if i.title == issue_title:
            issue = i
            break

    if issue:
        existing_body = issue.body
        new_body_lines = set(existing_body.split('\n'))
        for line in body.split('\n'):
            new_body_lines.add(line)
        new_body = '\n'.join(sorted(new_body_lines))
        issue.edit(body=new_body)
    else:
        issue = repo.create_issue(
            title=issue_title,
            body=f"The following alerts have been detected:\n{body}",
            labels=labels
        )
    return issue.html_url

def send_email_notification(from_address, to_address, smtp_server, smtp_port, subject, body):
    from email.mime.text import MIMEText
    import smtplib

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(from_address, [to_address], msg.as_string())
