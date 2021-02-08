#!/usr/bin/env bash

# Script to clean up project directory

rm -rf ./meraki_cli.egg-info

rm -rf build

rm -rf commit_env

rm -rf dist

rm -rf ".tox"

rm -rf ".pytest_cache"

rm -rf ".coverage"

rm -rf "coverage.xml"

rm -rf "htmlcov"

find . -type d -name "__pycache__*" -prune -execdir rm -rf {} \;  # Removal all '__pycache__' directories and their contents

find . -type f -name "*.pyc" -delete  # Removal all '.pyc' files

find . -name "*.log" -type f -delete  # Removal all '.log' files
