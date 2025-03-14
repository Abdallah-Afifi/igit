# igit: A Git-like Version Control System in Python

igit is a lightweight implementation of Git written in Python. It provides core version control functionality through a familiar command-line interface.

## Installation

```bash
git clone https://github.com/Abdallah-Afifi/igit.git
cd igit
python setup.py develop --user
mponents:

## Usage 

# Create a new repository
igit init

# Stage changes
igit add <file>

# Commit changes
igit commit -m "Commit message"

# View commit history
igit log

# Show commit details with diff
igit show <commit-id>

# Compare differences
igit diff
igit diff --cached
igit diff <commit>

# Create and manage branches
igit branch <branch-name>
igit checkout <branch-name>

# Create tags
igit tag <tag-name> [<commit-id>]

# Work with remotes
igit remote add <name> <url>
igit push <remote> <branch>
igit pull <remote> <branch>

## Requirements
Python 3.6+
No external dependencies beyond the standard library
