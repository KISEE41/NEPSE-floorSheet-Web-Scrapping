# GitHub Actions Workflow Documentation

This documentation provides an overview of the GitHub Actions workflow for web scraping implemented in this repository.

## Workflow Description

This GitHub Actions workflow automates web scraping tasks using a Python script. It is scheduled to run daily, except on Saturdays at 4 AM UTC. It runs on an **Ubuntu latest (ubuntu-latest)** environment. The primary goal of this workflow is to perform web scraping tasks using a Python script (`main.py`), record logs and store data files in csv format, and push the changes back to the GitHub repository.

```yaml
name: Web Scrapping

on:
  schedule:
    # Run everyday of the month except at saturday at 7PM
    - cron: 0 4 * * 0-5

jobs:
  build:
    runs-on: ubuntu-latest
```

## Workflow Steps

### 1. Checkout Repository Content

This step checks out the content of the repository to the GitHub runner.

```yaml
# checkout the repository content to github runner
- name: Checkout Repo Content
  uses: actions/checkout@v4
  with:
    ref: ${{ github.head_ref }}
```

_For more info about **action/Checkout@v4**, click **[here](https://github.com/actions/checkout)**_.

### 2. Set up Python 3.10

Configures the Python environment with version 3.10 using the `actions/setup-python@v4` action.

```yaml
# setting up python
- name: Set up Python 3.10
  uses: actions/setup-python@v4
  with:
    python-version: "3.10"
```

_For more info about **actions/setup-python@v4**, click **[here](https://github.com/actions/setup-pythont)**_.

### 3. Install Dependencies

Installs necessary Python dependencies specified in the `requirements.txt` file using `pip`.

```yaml
# Installing necessary dependencies specified in requirements.txt file
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install flake8 pytest
    pip install -r requirements.txt
```

### 4. Grant Execution Permission

Changes the mode to allow execution for the `main.py` file. \
(_While using linux based environment, the file should be made executable_)

```yaml
# Changing the mode to execution for executing the main.py file
- name: Granting Execution Permission
  run: chmod +x main.py
```

### 5. Execute The Script

Runs the Python script `main.py` to perform web scraping tasks.

```yaml
# Executing the python script
- name: Execute The Script
  run: python main.py
```

### 6. Commit Files

Configures the Git user information and adds any changes to the repository. Commits the changes with a message indicating updates to logs and uploaded data.

```yaml
# Generated logs and datas, and commit and push in github
- name: Commit Files
  run: |
    git config --local user.email "github-actions[bot]@users.noreply.github.com"
    git config --local user.name "github-actions[bot]"
    git add -A
    git diff-index --quiet HEAD || (git commit -a -m "updated logs, and uploaded datas" --allow-empty)
```

(_Note: A dummy user email and user name are configured as bot._)

### 7. Push Changes

Pushes the committed changes back to the `master` branch of the GitHub repository using the `ad-m/github-push-action@master` action.

```yaml
# Pushing the changes
- name: Push Changes
  uses: ad-m/github-push-action@master
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    branch: master
```

(_Note: **github_token: ${{ secrets.GITHUB_TOKEN }}** uses the token generated in github that is necessary for pushing the changes._)
_For more info about **ad-m/github-push-action@master**, click **[here](https://github.com/ad-m/github-push-action)**_.

## Workflow Triggers

The workflow is scheduled to run at 4:00 AM every day of the week except Saturday.

## Notes

- The workflow is designed to automate the process of web scraping and storing data files.
- It ensures that any changes made during the scraping process are committed and pushed back to the repository automatically.
- The Python environment is set up with version 3.10 to ensure compatibility with the dependencies and the script.
- The workflow utilizes various GitHub Actions to perform different tasks seamlessly.

This documentation provides an overview of the web scraping GitHub Actions workflow implemented in the repository.
