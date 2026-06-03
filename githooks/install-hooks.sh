#!/usr/bin/env bash
#
# install-hooks.sh — install Git hooks from the githooks/ directory.
#
# Usage:
#   ./githooks/install-hooks.sh
#
# This script copies (or symlinks) the project's Git hooks into .git/hooks/
# and makes them executable.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GIT_HOOKS_DIR="$PROJECT_ROOT/.git/hooks"

if [ ! -d "$GIT_HOOKS_DIR" ]; then
    echo "❌ Error: .git/hooks/ not found. Are you in a Git repository?"
    exit 1
fi

echo "🔧 Installing Git hooks from githooks/..."

for hook_file in "$SCRIPT_DIR"/*; do
    hook_name=$(basename "$hook_file")

    # Skip this install script itself
    if [ "$hook_name" = "install-hooks.sh" ]; then
        continue
    fi

    target="$GIT_HOOKS_DIR/$hook_name"

    # Remove existing hook or old sample
    if [ -L "$target" ]; then
        rm "$target"
    elif [ -f "$target" ]; then
        # Don't overwrite user's custom hooks — ask
        if grep -q "sample" "$target" 2>/dev/null || grep -q "githooks" "$target" 2>/dev/null; then
            rm "$target"
        else
            echo "⚠️  Skipping $hook_name — custom hook already exists at .git/hooks/$hook_name"
            continue
        fi
    fi

    # Create symlink (relative path for portability)
    ln -s "../../githooks/$hook_name" "$target"
    chmod +x "$target"
    echo "   ✅ $hook_name → .git/hooks/$hook_name"
done

echo ""
echo "🎉 Git hooks installed successfully!"
echo "   commit-msg: Enforces Jira ticket reference in commit messages"
echo ""
echo "   Format: <type>(<scope>): <description>  Refs: <TICKET-KEY>"
echo "   Example: feat(auth): add OAuth2 login  Refs: PROJ-123"
