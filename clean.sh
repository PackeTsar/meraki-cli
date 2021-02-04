#!/usr/bin/env bash

# Script to clean up project directory

rm -rf ./meraki_cli.egg-info

rm -rf build

rm -rf commit_env

rm -rf dist

find . -type d -name __pycache__ -prune -execdir rm -rf {} \;  # Removal all '__pycache__' directories and their contents

find . -type d -name env -prune -execdir rm -rf {} \;  # Removal all '__pycache__' directories and their contents

find . -type f -name "*.pyc" -delete  # Removal all '.pyc' files

find . -name "*.log" -type f -delete  # Removal all '.log' files
