# update.py
#
# 저장소를 원격(origin/master)에 맞춘다.
#
# 인코딩 주의 :
#   git 은 출력을 **UTF-8** 로 낸다. 반면 한국어 Windows 의 로케일은 cp949 라서
#   `subprocess.run(..., text=True)` 는 로케일로 디코딩하다 죽는다.
#   커밋 제목에 한글이 들어간 순간 `UnicodeDecodeError` 가 나고, 그 예외는
#   subprocess 의 리더 스레드에서 터지므로 **run() 은 조용히 stdout=None 을 돌려준다.**
#   읽기(encoding="utf-8")와 쓰기(콘솔 재설정) 양쪽을 다 고쳐야 한다.

import os
import sys
import subprocess


# 콘솔이 cp949 여도 git 출력(UTF-8)을 그대로 찍을 수 있게.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# 이 스크립트는 repo 루트의 scripts/ 하위에 있다 -> repo 루트는 한 단계 위.
# git 명령은 항상 repo 루트(cwd=ROOT)에서 실행해야 clean -fd 등이 전체에 적용된다.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_git(cmd):
    """git 명령 하나. 종료 코드를 돌려준다 (0 이면 성공)."""

    print("\n>>> " + " ".join(cmd))

    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        encoding="utf-8",       # git 출력은 UTF-8 (로케일 아님)
        errors="replace",       # 깨진 바이트가 있어도 죽지 않는다
    )

    if result.stdout:
        print(result.stdout.rstrip())

    if result.stderr:
        print(result.stderr.rstrip())

    if result.returncode != 0:
        print("[ERROR] git exited with %d" % result.returncode)

    return result.returncode


# 최신 정보 fetch -> 로컬 변경 강제 제거 -> 추적 안 되는 파일 제거
STEPS = [
    ["git", "fetch", "--all"],
    ["git", "reset", "--hard", "origin/master"],
    ["git", "clean", "-fd"],
]

failed = False

for step in STEPS:
    if run_git(step) != 0:
        failed = True
        break                   # 앞 단계가 실패했으면 뒤는 의미가 없다

print("\n========================================")

if failed:
    print("Update FAILED - see the error above")
    print("========================================\n")
    sys.exit(1)

print("Update Complete")
print("========================================\n")
