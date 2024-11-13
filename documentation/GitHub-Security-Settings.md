# GitHub Security Settings

## Best Practices for Configuring GitHub Advanced Security

### 1. Enable Code Scanning

- **Purpose**: Automatically detect vulnerabilities and coding errors in your codebase.
- **Configuration**:
  - Enable code scanning for all repositories.
  - Use GitHub's default CodeQL analysis or integrate with third-party tools.
  - Schedule regular scans (e.g., daily or weekly) to ensure continuous monitoring.

### 2. Enable Secret Scanning

- **Purpose**: Detect and prevent the inclusion of secrets (e.g., API keys, tokens) in your codebase.
- **Configuration**:
  - Enable secret scanning for all repositories.
  - Configure alerts to notify repository administrators and security teams when secrets are detected.
  - Regularly review and remediate detected secrets.

### 3. Enable Dependency Graph and Dependabot Alerts

- **Purpose**: Monitor and manage dependencies to identify and resolve vulnerabilities.
- **Configuration**:
  - Enable the dependency graph for all repositories.
  - Enable Dependabot alerts to receive notifications about vulnerable dependencies.
  - Enable Dependabot security updates to automatically open pull requests to resolve vulnerabilities.

### 4. Configure Branch Protection Rules

- **Purpose**: Protect important branches (e.g., `main`, `master`) from unauthorized changes.
- **Configuration**:
  - Require pull request reviews before merging.
  - Require status checks to pass before merging.
  - Enable branch protection for all critical branches.
  - Optionally, enable additional protections such as requiring signed commits and restricting who can push to the branch.

### 5. Use GitHub Environments for Secrets and Variables

- **Purpose**: Securely manage and control access to sensitive information.
- **Configuration**:
  - Create environments (e.g., `dev`, `qa`, `stg`, `prd`) to manage secrets and variables.
  - Store secrets and variables at the organization, repository, and environment levels as needed.
  - Use environment protection rules to control access to secrets and variables.

### 6. Monitor and Audit Security Events

- **Purpose**: Maintain visibility into security-related activities and changes.
- **Configuration**:
  - Enable GitHub audit logs to track changes to security settings, secrets, and other critical configurations.
  - Regularly review audit logs to identify and investigate suspicious activities.
  - Set up alerts for critical security events.

### 7. Implement Access Controls and Permissions

- **Purpose**: Ensure that only authorized users have access to sensitive repositories and settings.
- **Configuration**:
  - Use GitHub Teams to manage user access and permissions.
  - Apply the principle of least privilege, granting users the minimum necessary permissions.
  - Regularly review and update access controls to ensure they align with current organizational needs.

### 8. Educate and Train Developers

- **Purpose**: Promote security awareness and best practices among developers.
- **Configuration**:
  - Provide training on secure coding practices and GitHub security features.
  - Encourage developers to regularly review and address security alerts.
  - Foster a culture of security within the development team.

### 9. Regularly Review and Update Security Policies

- **Purpose**: Ensure that security policies remain effective and up-to-date.
- **Configuration**:
  - Regularly review and update security configurations and policies.
  - Stay informed about new GitHub security features and best practices.
  - Conduct periodic security assessments to identify and address potential gaps.

By following these best practices, you can effectively configure GitHub Advanced Security to protect your repositories and organization from security threats.

---
## Organization Settings

### Security Configuration

To ensure your GitHub organization is secure, follow these steps to configure the recommended security settings.

1. **Navigate to Organization Settings**
   - Go to your GitHub organization.
   - Click on the organization name in the top-right corner.
   - Select **Settings** from the dropdown menu.

2. **Access Security Settings**
   - In the left sidebar, click on **Security**.
   - Under the **Security** section, select **Code security and analysis**.

3. **Create a New Security Configuration**
   - Scroll down to the **Configurations** section.
   - Click on **Add configuration**.

4. **Configure Security Settings**
   - Name the configuration **Quest Recommended**.
   - Use all of the GitHub recommended settings.
   - Additionally, enable the following:
     - **Security updates** under **Dependency graph**.
     - **Dependabot alerts and security updates** to allow Dependabot to automatically open pull requests to resolve alerts.

5. **Save Configuration**
   - Review the settings to ensure they match the recommended configuration.
   - Click **Save** to apply the configuration.

### Recommended Settings

The **Quest Recommended** configuration includes the following GitHub recommended settings:

- **Code scanning**: Enable code scanning to automatically detect vulnerabilities in your code.
- **Secret scanning**: Enable secret scanning to detect and prevent the inclusion of secrets in your codebase.
- **Dependency graph**: Enable the dependency graph to visualize and manage your project's dependencies.
  - **Security updates**: Enable this to receive automatic security updates for your dependencies.
- **Dependabot alerts and security updates**: Enable Dependabot to automatically open pull requests to resolve security alerts.

By following these steps, you ensure that your GitHub organization is configured with the best security practices, including automatic dependency updates and vulnerability scanning.

## Global Settings

### Bypass Push Protection

To manage push protection settings and allow certain teams to bypass them, follow these steps:

1. **Navigate to Global Settings**
   - Go to your GitHub organization.
   - Click on the organization name in the top-right corner.
   - Select **Settings** from the dropdown menu.

2. **Access Push Protection Settings**
   - In the left sidebar, click on **Security**.
   - Under the **Security** section, select **Push protection**.

3. **Configure Bypass List**
   - Add the following team to the bypass list: `azrgh-team-DSO-Platformadmins-1`.
   - This team will have the ability to bypass push protection when necessary.

4. **Request Process for Bypass**
   - Everyone else will need to submit a request to bypass push protection.
   - GitHub administrators can review these requests and grant bypass permissions when there is a legitimate regulatory, business, or security exemption required to achieve a particular task or requirement.

By configuring these settings, you provide a controlled way for certain teams to bypass push protection while ensuring that all other users follow the standard request process.

---

# Storing Actions Secrets and Variables in GitHub

## Why Store Actions Secrets and Variables in GitHub?

Storing Actions secrets and variables in GitHub provides several benefits:

1. **Security**: GitHub encrypts secrets and variables, ensuring that sensitive information such as API keys, tokens, and passwords are securely stored and accessed only by authorized workflows.
2. **Centralized Management**: By storing secrets and variables in GitHub, you can manage them centrally, making it easier to update and maintain them across multiple workflows and repositories.
3. **Access Control**: GitHub allows you to control access to secrets and variables at different levels (organization, repository, and environment), ensuring that only the necessary workflows and users have access to sensitive information.
4. **Auditability**: GitHub provides audit logs that track changes to secrets and variables, helping you maintain a record of who accessed or modified them.

## How to Create and Use GitHub Environments to Store Secrets and Variables

### Organization Level

1. **Navigate to Organization Settings**
   - Go to your GitHub organization.
   - Click on the organization name in the top-right corner.
   - Select **Settings** from the dropdown menu.

2. **Access Secrets and Variables**
   - In the left sidebar, click on **Secrets and variables**.
   - Select **Actions**.

3. **Add a New Secret or Variable**
   - Click on **New organization secret** or **New organization variable**.
   - Enter a name and value for the secret or variable.
   - Click **Add secret** or **Add variable** to save.

### Repository Level

1. **Navigate to Repository Settings**
   - Go to your GitHub repository.
   - Click on the repository name in the top-right corner.
   - Select **Settings** from the dropdown menu.

2. **Access Secrets and Variables**
   - In the left sidebar, click on **Secrets and variables**.
   - Select **Actions**.

3. **Add a New Secret or Variable**
   - Click on **New repository secret** or **New repository variable**.
   - Enter a name and value for the secret or variable.
   - Click **Add secret** or **Add variable** to save.

### Repository Environment Level

1. **Navigate to Repository Settings**
   - Go to your GitHub repository.
   - Click on the repository name in the top-right corner.
   - Select **Settings** from the dropdown menu.

2. **Access Environments**
   - In the left sidebar, click on **Environments**.
   - Click on **New environment** to create a new environment or select an existing environment.

3. **Add Secrets and Variables to the Environment**
   - Click on the environment name.
   - Under the **Secrets and variables** section, click on **Add secret** or **Add variable**.
   - Enter a name and value for the secret or variable.
   - Click **Add secret** or **Add variable** to save.

4. **Standard Environments for QDX**
   - The standard environments for QDX will be `dev`, `qa`, `stg`, and `prd`.
   - To ensure compatibility with reusable workflows, composite actions, and repository templates throughout the enterprise, it is imperative that these naming standards be followed.

## Using Secrets and Variables in Workflows

To use secrets and variables in your GitHub Actions workflows, reference them in your workflow YAML files as follows:

### Example Workflow

```yaml
name: Example Workflow

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Use secret and variable
      run: "Secret: ${{ secrets.MY_SECRET }} and Variable: ${{ vars.MY_VARIABLE }}"
```

In this example, `MY_SECRET` and `MY_VARIABLE` are referenced from the secrets and variables stored at the organization, repository, or environment level.

By following these steps, you can securely store and manage your GitHub Actions secrets and variables, ensuring that your workflows have access to the necessary sensitive information while maintaining security and control.

---

# Why Use GitHub Apps Over Personal Access Tokens

## Advantages of GitHub Apps

### 1. **Granular Permissions**
GitHub Apps offer more granular permissions compared to personal access tokens. You can specify exactly what the app can and cannot do, reducing the risk of over-permissioned tokens.

### 2. **Scoped Access**
GitHub Apps can be installed on specific repositories or the entire organization, providing scoped access to only the resources they need. This minimizes the potential impact of a compromised token.

### 3. **Enhanced Security**
GitHub Apps use short-lived tokens that are automatically rotated, reducing the risk of long-term exposure. Personal access tokens, on the other hand, are long-lived and require manual rotation.

### 4. **Auditability**
Actions performed by GitHub Apps are logged and attributed to the app, providing better audit trails and accountability. This makes it easier to track changes and identify the source of actions.

### 5. **Separation of Concerns**
GitHub Apps can be managed independently of individual user accounts, ensuring that organizational workflows and integrations are not disrupted by changes to personal accounts.

## How to Create and Configure a GitHub App

### Step 1: Create the GitHub App

1. **Navigate to GitHub App Settings**
   - Go to your GitHub organization.
   - Click on the organization name in the top-right corner.
   - Select **Settings** from the dropdown menu.
   - In the left sidebar, click on **Developer settings**.
   - Click on **GitHub Apps**.

2. **Create a New GitHub App**
   - Click on **New GitHub App**.
   - Fill in the required details:
     - **GitHub App name**: Choose a name for your app.
     - **Homepage URL**: Provide a URL for the app's homepage.
     - **Webhook URL**: (Optional) Provide a URL to receive webhook events.
     - **Webhook secret**: (Optional) Provide a secret to secure webhook payloads.
   - Configure the **Permissions & events**:
     - Select the permissions your app needs.
     - Subscribe to the events your app should receive.
   - Click **Create GitHub App**.

### Step 2: Generate and Store Keys

1. **Generate a Private Key**
   - After creating the app, navigate to the app's settings page.
   - In the left sidebar, click on **Private keys**.
   - Click on **Generate a private key**.
   - Download the private key file (`.pem`) and store it securely.

2. **Store the Private Key in GitHub Secrets**
   - Navigate to your GitHub organization or repository settings.
   - In the left sidebar, click on **Secrets and variables**.
   - Select **Actions**.
   - Click on **New organization secret** or **New repository secret**.
   - Name the secret (e.g., `GITHUB_APP_PRIVATE_KEY`) and paste the contents of the private key file.
   - Click **Add secret** to save.

### Step 3: Install the GitHub App

1. **Install the App**
   - Navigate to the app's settings page.
   - In the left sidebar, click on **Install App**.
   - Click on **Install** next to the organization or repository where you want to install the app.
   - Select the repositories the app should have access to, or choose **All repositories**.
   - Click **Install** to complete the installation.

### Example: Using the GitHub App Token in a Workflow to Retrieve Repository Details

Below is an example GitHub Actions workflow that generates a GitHub App token and uses it to retrieve the details of an internal repository using the GitHub API:

```yaml
# Retrieve details of an internal repository using the GitHub API
name: 'Retrieve Repository Details'
on:
  workflow_dispatch:
    inputs:
      repository_name:
        description: 'Name of the repository'
        required: true
        type: string
    secrets:
      app-id:
        description: 'GitHub App ID'
        required: true
      private-key:
        description: 'Private Key for the GitHub App'
        required: true

jobs:
  retrieve_repo_details:
    runs-on: ubuntu-latest
    steps:
      - name: Generate a token
        id: generate-token
        uses: actions/create-github-app-token@v1
        with:
          app-id: ${{ secrets.app-id }}
          private-key: ${{ secrets.private-key }}
    
      - name: Retrieve Repository Details
        id: get_repo_details
        run: |
          REPO_DETAILS=$(curl -s \
            -H "Authorization: Bearer ${{ steps.generate-token.outputs.token }}" \
            -H "Accept: application/vnd.github.v3+json" \
            "${{ github.api_url }}/repos/${{ github.repository_owner }}/${{ inputs.repository_name }}")
          echo "$REPO_DETAILS"
          echo "::set-output name=repo_details::$REPO_DETAILS"

      - name: Display Repository Details
        run: |
          echo "Repository Details: ${{ steps.get_repo_details.outputs.repo_details }}"
```

In this example, the workflow:
1. Generates a GitHub App token using the `actions/create-github-app-token@v1` action.
2. Uses the generated token to retrieve the details of the specified repository using the GitHub API.
3. Displays the retrieved repository details.

By following these steps, you can create, configure, and install a GitHub App with the appropriate permissions and securely manage its keys. This approach provides enhanced security, granular permissions, and better auditability compared to using personal access tokens.

---
