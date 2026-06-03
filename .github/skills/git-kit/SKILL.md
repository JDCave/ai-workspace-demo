---
name: git-kit
description: Perform common Git operations — diff, log, branch management, blame. Use this when the user asks about code changes, commit history, branch status, or blame information.
allowed-tools: shell
---

# Git Operations Skill

You have access to a Python CLI tool for common Git operations including diff viewing, commit log inspection, branch management, blame annotation, and repository status.

## When to Use
- User wants to view code changes or diffs between branches
- User asks about commit history or recent changes
- User needs to create, list, or delete branches
- User wants to see who last modified specific lines of code (blame)
- User wants to check the working tree status

## Available Commands

### Diff
```bash
python .github/skills/git-kit/git_tool.py diff [--branch main] [--stat]
```

**Parameters:**
- `--branch`: Target branch to compare against (default: `main`)
- `--stat`: Show only stat summary instead of full diff

### Log
```bash
python .github/skills/git-kit/git_tool.py log [--count 10] [--branch main] [--author] [--since]
```

**Parameters:**
- `--count`: Number of commits to return (default: `10`)
- `--branch`: Branch to inspect (default: `main`)
- `--author`: Filter commits by author name or email
- `--since`: Only commits after this date (e.g. `2025-01-01`)

### Branch
```bash
python .github/skills/git-kit/git_tool.py branch [--list] [--create <name>] [--delete <name>]
```

**Parameters:**
- `--list`: List all local and remote branches
- `--create`: Create a new branch with the given name
- `--delete`: Delete the specified branch

### Blame
```bash
python .github/skills/git-kit/git_tool.py blame --file <path> [--lines]
```

**Parameters:**
- `--file` (required): Path to the file to blame
- `--lines`: Line range to inspect (e.g. `10-20`)

### Status
```bash
python .github/skills/git-kit/git_tool.py status
```

Shows the current working tree status including staged, unstaged, and untracked files.

## Important Rules
- **ALWAYS** run `status` first before performing branch operations to understand the current state
- Use `diff --stat` for a quick overview before showing full diffs
- **NEVER** delete a branch without user confirmation
- When showing log results, summarize key changes rather than dumping raw output
- For blame, always provide the file path relative to the repository root

## Configuration
Requires `.env` file with:
```
GIT_REPO_PATH=/path/to/your/repository
```
