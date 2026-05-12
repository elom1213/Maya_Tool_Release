import subprocess
import os

ROOT = os.path.dirname(__file__)


def run_git(cmd):

    print(f"\n>>> {' '.join(cmd)}")

    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        shell=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)


# 최신 정보 fetch
run_git(["git", "fetch", "--all"])

# 로컬 변경 강제 제거
run_git(["git", "reset", "--hard", "origin/master"])

# 추적 안 되는 파일 제거
run_git(["git", "clean", "-fd"])

print("========================================")
print("\nUpdate Complete")
print("========================================\n")