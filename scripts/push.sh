#!/usr/bin/env bash
# Push Machina Caeli to the company GitHub and Hugging Face.
# Create both empty repos (lastelleai/machina-caeli) first, then run:
#   ./scripts/push.sh
# Auth: `gh auth login` for GitHub; a Hugging Face write token for HF
# (git will prompt; username = your HF username, password = the token).
set -euo pipefail

GITHUB_ORG="lastelleai"   # company GitHub account
HF_ORG="lastelleai"       # company Hugging Face account
REPO="machina-caeli"

cd "$(dirname "$0")/.."

git lfs install
[[ -d .git ]] || git init -b main
git add -A
git diff --cached --quiet || git commit -m "Machina Caeli: initial release"

git remote get-url github >/dev/null 2>&1 || git remote add github "https://github.com/${GITHUB_ORG}/${REPO}.git"
git remote get-url hf     >/dev/null 2>&1 || git remote add hf     "https://huggingface.co/${HF_ORG}/${REPO}"

git push -u github main
git push -u hf main
