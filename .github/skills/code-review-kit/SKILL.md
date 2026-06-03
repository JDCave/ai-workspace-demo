---
name: code-review-kit
description: Automate code review workflows — analyze diffs, check coding standards, detect security issues, generate review comments. Use this when the user asks for code review, PR analysis, or code quality checks.
allowed-tools: shell
---

# Code Review Automation Skill

You have access to a Python CLI tool for automated code review workflows including diff analysis, coding standards checks, security issue detection, and review comment generation.

## When to Use
- User wants to analyze a diff between branches or commits for code quality
- User wants to check files or directories against coding standards
- User wants to scan code for security vulnerabilities
- User wants to generate structured review comments on specific files/lines
- User asks for a PR review, code review, or code quality assessment

## Available Commands

### Analyze Diff
Analyze code changes between a source branch/commit and a target branch.
```bash
python .github/skills/code-review-kit/review_tool.py analyze --source <branch_or_commit> [--target main] [--severity warning]
```
**Parameters:**
- `--source` (required): Branch name or commit hash to analyze from
- `--target`: Target branch to compare against (default: `main`)
- `--severity`: Minimum severity level to report — `info`, `warning`, `error` (default: `warning`)

### Check Coding Standards
Validate files or directories against configurable coding rules.
```bash
python .github/skills/code-review-kit/review_tool.py standards --path <file_or_dir> [--ruleset default|strict]
```
**Parameters:**
- `--path` (required): File or directory path to check
- `--ruleset`: Rule set to apply — `default` or `strict` (default: `default`)

### Security Scan
Scan files or directories for common security vulnerabilities.
```bash
python .github/skills/code-review-kit/review_tool.py security --path <file_or_dir> [--severity medium]
```
**Parameters:**
- `--path` (required): File or directory path to scan
- `--severity`: Minimum severity to report — `low`, `medium`, `high`, `critical` (default: `medium`)

### Generate Review Comment
Create a structured review comment for a specific file and line.
```bash
python .github/skills/code-review-kit/review_tool.py comment --file <path> --line <num> --message "<text>"
```
**Parameters:**
- `--file` (required): File path the comment applies to
- `--line` (required): Line number the comment targets
- `--message` (required): Review comment text (enclose in quotes)

## Parameters

| Parameter | Commands | Required | Default | Description |
|-----------|----------|----------|---------|-------------|
| `--source` | analyze | Yes | — | Source branch or commit hash |
| `--target` | analyze | No | `main` | Target branch for comparison |
| `--severity` | analyze, security | No | `warning` / `medium` | Minimum severity threshold |
| `--path` | standards, security | Yes | — | File or directory to inspect |
| `--ruleset` | standards | No | `default` | `default` or `strict` rule set |
| `--file` | comment | Yes | — | Target file path |
| `--line` | comment | Yes | — | Line number |
| `--message` | comment | Yes | — | Comment text |

## Important Rules
- **ALWAYS** run an analyze or security scan before generating review comments to ensure findings are grounded in actual results
- **ALWAYS** present findings to the user in a clear, prioritized summary before generating automated comments
- Use `--severity` filtering to avoid overwhelming the review with low-priority items
- When reviewing a PR, run `analyze` on the diff first, then `standards` and `security` on changed files for comprehensive coverage
- **NEVER** auto-submit review comments without user confirmation — show a preview first
- For large changesets, break the review into per-directory scans to keep output manageable

## Configuration
Requires `.env` file in the project root with:
```
# Optional: GitHub token for fetching PR/branch data
GITHUB_TOKEN=ghp_your_token_here

# Optional: Custom review rules directory
REVIEW_RULES_DIR=.github/code-review-rules

# Optional: Default target branch
DEFAULT_TARGET_BRANCH=main
```
