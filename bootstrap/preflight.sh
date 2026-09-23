#!/usr/bin/env bash
set +e

echo "=== Potencia IA preflight (macOS/Linux) ==="
echo "OS: $(uname -s)"
echo "Architecture: $(uname -m)"
echo "Shell: ${SHELL:-unknown}"

commands=(claude git python python3 node npm uv pipx codex docker brew)

for cmd in "${commands[@]}"; do
  if command -v "$cmd" >/dev/null 2>&1; then
    version="$("$cmd" --version 2>&1 | head -n 1)"
    echo "$cmd: FOUND | $version"
  else
    echo "$cmd: NOT FOUND"
  fi
done

echo
echo "Diagnostic only. Installation/activation follows bootstrap/BOOTSTRAP.md."
