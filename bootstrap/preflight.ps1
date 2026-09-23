$ErrorActionPreference = "Continue"

Write-Host "=== Potencia IA preflight (Windows) ==="
Write-Host "OS: Windows"
Write-Host "Architecture: $env:PROCESSOR_ARCHITECTURE"

$commands = @(
  "claude", "git", "python", "python3", "node", "npm",
  "uv", "pipx", "codex", "docker", "winget"
)

foreach ($cmd in $commands) {
  $found = Get-Command $cmd -ErrorAction SilentlyContinue
  if ($found) {
    try {
      $version = & $cmd --version 2>&1 | Select-Object -First 1
      Write-Host ("{0}: FOUND | {1}" -f $cmd, $version)
    } catch {
      Write-Host ("{0}: FOUND | version unavailable" -f $cmd)
    }
  } else {
    Write-Host ("{0}: NOT FOUND" -f $cmd)
  }
}

Write-Host ""
Write-Host "Diagnostic only. Installation/activation follows bootstrap/BOOTSTRAP.md."
