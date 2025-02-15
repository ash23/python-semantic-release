#!/bin/bash

set -e

# Copy inputs into correctly-named environment variables
export GH_TOKEN="${INPUT_GITHUB_TOKEN}"
export PYPI_TOKEN="${INPUT_PYPI_TOKEN}"
export REPOSITORY_USERNAME="${INPUT_REPOSITORY_USERNAME}"
export REPOSITORY_PASSWORD="${INPUT_REPOSITORY_PASSWORD}"
export PATH="${PATH}:/semantic-release/.venv/bin"
export GIT_COMMITTER_NAME="${INPUT_GIT_COMMITTER_NAME:="github-actions"}"
export GIT_COMMITTER_EMAIL="${INPUT_GIT_COMMITTER_EMAIL:="github-actions@github.com"}"

# Change to configured directory
cd "${INPUT_DIRECTORY}"

# Set Git details
git config --global user.name "$GIT_COMMITTER_NAME"
git config --global user.email "$GIT_COMMITTER_EMAIL"

# Run Semantic Release
/semantic-release/.venv/bin/python \
  -m semantic_release publish \
  -v DEBUG \
  -D commit_author="$GIT_COMMITTER_NAME <$GIT_COMMITTER_EMAIL>" \
  ${INPUT_ADDITIONAL_OPTIONS}
