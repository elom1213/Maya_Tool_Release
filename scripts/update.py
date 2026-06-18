import subprocess
import os

# 이 스크립트는 repo 루트의 scripts/ 하위에 있다 → repo 루트는 한 단계 위.
# git 명령은 항상 repo 루트(cwd=ROOT)에서 실행해야 clean -fd 등이 전체에 적용된다.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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
print("Update Complete")
print("========================================\n")