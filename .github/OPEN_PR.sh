#!/usr/bin/env bash
# Open PR using GitHub CLI. This script tries to detect the default branch; update BASE if detection fails.
set -e
REPO="$(git remote get-url origin | sed -E 's#.*[:/]([^/]+/[^/]+)(\.git)?$#\1#')"
# Try to detect default branch with gh; fallback to main
DEFAULT_BRANCH="$(gh repo view --json defaultBranchRef -q .defaultBranchRef.name 2>/dev/null || echo main)"
HEAD_BRANCH="feature/add-final-projects"
TITLE="Add runnable project scaffolding and recruiter checklist"
BODY_FILE=".github/PR_BODY.md"

echo "Repo: $REPO"
echo "Default branch detected: $DEFAULT_BRANCH"
echo "Creating PR from $HEAD_BRANCH -> $DEFAULT_BRANCH"

gh pr create --title "$TITLE" --body-file "$BODY_FILE" --base "$DEFAULT_BRANCH" --head "$HEAD_BRANCH" || {
  echo "gh pr create failed. Please run the following command manually:" 
  echo "gh pr create --title \"$TITLE\" --body-file \"$BODY_FILE\" --base $DEFAULT_BRANCH --head $HEAD_BRANCH"
  exit 1
}
