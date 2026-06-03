---
name: test-runner-kit
description: Run tests, collect coverage reports, and analyze test gaps. Use this when the user asks to run unit/integration tests, check code coverage, or find untested code.
allowed-tools: shell
---

# Test Runner Kit Skill

You have access to a Python CLI tool for running tests, collecting coverage reports, and identifying untested code.

## When to Use
- User wants to run unit or integration tests
- User wants to check code coverage metrics
- User wants to find untested code or test gaps
- After making code changes, user wants to verify tests pass
- User asks for a test plan or wants to understand test coverage

## Available Commands

### Run Tests
```bash
python .github/skills/test-runner-kit/test_tool.py run [--type unit|integration|all] [--path] [--verbose]
```

**Parameters:**
- `--type` (required): Type of tests to run — `unit`, `integration`, or `all`. Default: `all`
- `--path`: Specific file or directory to test. Default: project root
- `--verbose`: Enable verbose output with detailed test results

### Collect Coverage
```bash
python .github/skills/test-runner-kit/test_tool.py coverage [--format text|json] [--threshold 80]
```

**Parameters:**
- `--format`: Output format — `text` (human-readable) or `json`. Default: `text`
- `--threshold`: Minimum coverage percentage to pass. Default: `80`

### Analyze Test Gaps
```bash
python .github/skills/test-runner-kit/test_tool.py gaps [--path]
```

**Parameters:**
- `--path`: Specific directory to analyze for test gaps. Default: project root

## Parameters

| Parameter    | Command(s)  | Required | Description                                      |
|-------------|-------------|----------|--------------------------------------------------|
| `--type`    | run         | No       | Test type: `unit`, `integration`, or `all`       |
| `--path`    | run, gaps   | No       | Target file or directory                         |
| `--verbose` | run         | No       | Show detailed test output                        |
| `--format`  | coverage    | No       | Output format: `text` or `json`                  |
| `--threshold` | coverage  | No       | Minimum coverage % to consider passing (default: 80) |

## Important Rules
- **ALWAYS** dry-run first: preview what tests will be executed before running them
- **ALWAYS** show the test plan to the user before executing (list test files, expected count)
- Report a summary after execution: total tests, passed, failed, skipped
- When analyzing coverage, highlight files below the threshold
- When identifying gaps, suggest specific test cases that should be added

## Configuration
Requires `.env` file with:
```
TEST_RUNNER=pytest
COVERAGE_TOOL=coverage.py
```
