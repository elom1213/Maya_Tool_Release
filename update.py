import subprocess
import os

ROOT = os.path.dirname(__file__)

print("Pulling latest version...")

result = subprocess.run(
    ["git", "pull"],
    cwd=ROOT,
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)
