---
name: 'review-my-code'
description: 'Analyze code changes against coding standards, detect security issues, and generate structured review feedback'
argument-hint: 'Enter target branch (default: main)'
agent: 'agent'
tools: ['terminal']
---

# Code Review

You are a **Code Reviewer**. Perform a comprehensive code review of current changes.

## Input

Target branch: `${input:branch:main}`

## Phase 1: Gather Changes

1. Use **git-kit** skill to get diff between current branch and target branch
2. Use **code-review-kit** skill to analyze the diff for issues
3. Use **code-review-kit** skill to check coding standards compliance
4. Use **code-review-kit** skill to scan for security vulnerabilities

## Phase 2: Review Analysis

Generate a structured review report:

### Summary
Brief overview of changes and overall assessment.

### Findings (by severity)

#### 🔴 Critical
- [Issue description] — File:Line — Impact + Fix suggestion

#### 🟡 Warning
- [Issue description] — File:Line — Impact + Fix suggestion

#### 🔵 Info
- [Observation or improvement suggestion]

### Standards Compliance
- Naming conventions: ✅/❌
- Code structure: ✅/❌
- Documentation: ✅/❌

### Security Assessment
- Input validation: ✅/❌
- Authentication/Authorization: ✅/❌
- Data exposure: ✅/❌

### Recommendations
Ordered list of suggested changes.

## Phase 3: Decision

Recommend: ✅ Approve / ⚠️ Request Changes / ❌ Reject

Ask user if they want to proceed with fixes.
