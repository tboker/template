1. # GitLab to GitHub Enterprise Cloud (GHEC) migration playbook

This playbook is a step-by-step guide to assist you with migration from [GitLab](https://GitLab.com) to [GitHub.com Enterprise Cloud](https://GitHub.com) **GHEC**.

| Steps & Tasks | Description |
| --- | --- |
| Step One | An overview of what is required to start the migration process|
| Step Two  | Use the gl_exporter utility to create an artifact of the gitlab repositories to migrate |
| Step Three | With the file ready to be imported, this step will guide you on how to connect and upload the file to your GitHub Enterprise Cloud instance. |
| Step Four | Once the repository is migrated, set it up for common use cases. |

## Step One
###### Preparing the ground for migration


For instance, GitLab uses a different naming convention than GitHub for things, as a quick reference, use the table below to upgrade your GitLab lingo into GitHub.


#### Naming convention 

| GitLab  | GitHub |
| --- | --- |
| Groups  | Organizations |
| Group members  | Teams |
| Projects  | Repositories |
| Merge Requests  | Pull Requests |
| Merge Request Notes | Issue comments |
| Issue notes | Issue comments |

#### Limitations

The tools used to support Gitlab to Github are constantly evolving to support new things, however, the interoperability between GitLab and GitHub, may lead to some issues during your migration process, please check what you *can* and *can't* do while using the tools.

##### Tasks

- [ ] Check the [Github Enterprise Migration Guide](https://github.github.com/enterprise-migrations/#/)
- [ ] Make a list of all repositories that need to be migrated
- [ ] Categorize/Group the repositories depending on the different source platforms
- [ ] Create a source-to-target matrix/checklist for each of the categorized/grouped repositories
- [ ] Determine potential Organizations that will be created in the target platform
- [ ] Check the [scope of the migration](https://GitHub.GitHub.com/enterprise-migrations/#/./1.4-pre-migration-scope) to be executed

## Step Two
###### Export data from GitLab
Try to create simple groupings with no more than 5-10 repositories, depending on the size of the repositories.

##### Tasks

- [ ] Utilize the [gl_exporter utility] (https://github.com/QDXDSOSandboxOrg/gl-exporter-1.7.1)

`If you run into an issue with a user that has been blocked, you will need to modify the code and replace that particular user with an active user as a work around.  Otherwise, you will continue to get a null pointer exception and the migration will not be able to proceed.  Use the code example below`

[gitlab.rb](https://github.com/QDXDSOSandboxOrg/gl-exporter-1.7.1/blob/0b15688ecf560419b5d0e0376e8593682fd505ba/lib/gitlab.rb#L123)
``` 
    # Get a single user by username
    #
    # @param [String] username the username of the user
    #   you want to fetch
    # @return [Hash] The returned user
    def user_by_username(username)
      # Check if the username matches the blocked user and change it
      if username == "questdiagnostics-import-admin"
        username = "<USER ID FOR AN ACTIVE USER>"         <---- This is the important line to change
      end
   
      get("users?username=#{username}").first
    end
```

## Step Three
###### Import data from GitLab

##### Tasks

- [ ] Follow the [steps](https://github.github.com/enterprise-migrations/#/./3.1.1-import-from-archive) to upload the archive file to Github Enterprise Cloud 
- [ ] Follow [post migration](https://github.github.com/enterprise-migrations/#/./4.0-post-migration-diagram) steps to ensure the repository has all you require

## Step Four
###### Configure repository settings

##### Tasks
1.    Ensure repository visibility is 'internal'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Settings -> Danger Zone -> Changerepository visibility

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Select 'Change visibility' internal

2.     Enable Github Actions

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Settings -> Actions -> General

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Actions permissions -> Allow enterprise, andselect non-enterprise, actions and reusable workflows

3.     Create GitHub Environments

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;· Settings -> Code and automations ->Environments

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     New environment (create dev, qa, stg, and prdenvironments)

4.    Transfer GitLab repository and environmentvariables and/or secrets to GitHub

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Settings -> Security -> Secrets andvariables -> Actions

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Select the appropriate tab for Secrets orVariables

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;·     Create the respective key/value pairs 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\*\* Once a secret is saved inGithub, you will no longer be able to display the value \*\***
