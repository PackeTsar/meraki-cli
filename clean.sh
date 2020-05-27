#!/usr/bin/env bash

# Script to clean up project directory

find . -type d -name __pycache__ -prune -execdir rm -rf {} \;  # Removal all '__pycache__' directories and their contents

find . -type d -name env -prune -execdir rm -rf {} \;  # Removal all '__pycache__' directories and their contents

find . -type f -name "*.pyc" -delete  # Removal all '.pyc' directories and their contents
