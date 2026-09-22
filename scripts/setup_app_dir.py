# setup_app_dir.py
#
# Maya 의 userSetup.py 에 이 저장소의 tools 경로를 등록한다.
#
# 마야는 **`userSetup.py` 라는 이름의 파일만** 실행한다.
# 예전에는 기존 파일을 덮어쓰지 않으려고 `userSetup_001.py`, `_002.py` ... 로 번호를 붙여
# 새 파일을 만들었는데, 그렇게 만든 파일은 **마야가 아예 읽지 않는다** —
# 두 번째 설치부터는 경로 등록이 조용히 무효가 됐다.
#
# 그래서 이제는 파일을 하나만 쓰고, 그 안에서 **표식으로 감싼 우리 블록만** 갈아 끼운다.
#   - 사용자가 직접 써 둔 내용은 그대로 둔다
#   - 몇 번을 돌려도 결과가 같다 (idempotent)
#   - 저장소를 다른 경로로 옮겨도 다음 설치에서 경로가 갱신된다

import os
import sys
import glob
import getpass


# 콘솔이 cp949 여도 깨지지 않게 (경로에 비 ASCII 가 섞일 수 있다)
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


BEGIN = "# >>> JUN TOOLS >>>"
END = "# <<< JUN TOOLS <<<"


# =========================
# CURRENT TOOL ROOT
# =========================

# 이 스크립트는 repo 루트의 scripts/ 하위에 있다 -> repo 루트는 한 단계 위.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_ROOT = os.path.join(REPO_ROOT, "tools")

# Maya 에서 경로 문제 줄이기 위해 / 로 통일
TOOLS_ROOT = TOOLS_ROOT.replace("\\", "/")


# =========================
# MAYA SCRIPTS DIR
# =========================

username = getpass.getuser()

maya_scripts_dir = os.path.join(
    "C:/Users",
    username,
    "Documents",
    "maya",
    "scripts"
)

maya_scripts_dir = maya_scripts_dir.replace("\\", "/")

os.makedirs(maya_scripts_dir, exist_ok=True)

user_setup_path = os.path.join(maya_scripts_dir, "userSetup.py").replace("\\", "/")


# =========================
# OUR BLOCK
# =========================

def build_block(tools_root):
    """표식으로 감싼 우리 블록 한 덩어리."""

    return (
        BEGIN + "\n"
        "import sys\n"
        "\n"
        'TOOLS_ROOT = r"' + tools_root + '"\n'
        "\n"
        "if TOOLS_ROOT not in sys.path:\n"
        "    sys.path.append(TOOLS_ROOT)\n"
        "\n"
        'print("JUN Tools Loaded")\n'
        + END + "\n"
    )


def merge_block(text, block):
    """기존 내용에 블록을 끼워 넣는다. 이미 있으면 그 자리만 교체.

    돌려주는 값은 (새 내용, 무엇을 했는지) 두 개.
    """

    if BEGIN in text and END in text:

        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)

        return head + block + tail.lstrip("\n"), "updated"

    if text.strip():
        return text.rstrip() + "\n\n" + block, "appended"

    return block, "created"


# =========================
# WRITE
# =========================

existing = ""

if os.path.exists(user_setup_path):
    with open(user_setup_path, encoding="utf-8") as f:
        existing = f.read()

new_text, action = merge_block(existing, build_block(TOOLS_ROOT))

if new_text != existing:
    with open(user_setup_path, "w", encoding="utf-8") as f:
        f.write(new_text)
else:
    action = "unchanged"


# =========================
# DONE
# =========================

print("========================================")
print("userSetup.py %s" % action)
print(user_setup_path)
print("tools path : %s" % TOOLS_ROOT)
print("========================================")


# 옛 방식이 남긴, 마야가 읽지 않는 파일들을 알려준다 (지우지는 않는다).
strays = sorted(glob.glob(os.path.join(maya_scripts_dir, "userSetup_[0-9][0-9][0-9].py")))

if strays:
    print("")
    print("NOTE: Maya only runs a file named exactly 'userSetup.py'.")
    print("      These were made by the old installer and are never executed.")
    print("      They are left untouched - delete them if you do not need them:")

    for path in strays:
        print("        " + path.replace("\\", "/"))

    print("")
