# setUp_app_dir.py

import os
import sys
import getpass


# =========================
# USER NAME
# =========================

username = getpass.getuser()
# setupFile_name = "userSetup.py"
setupFile_name = "userSetup.py"

# =========================
# CURRENT TOOL ROOT
# =========================

# 이 스크립트는 repo 루트의 scripts/ 하위에 있다 → repo 루트는 한 단계 위.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_ROOT = os.path.join(REPO_ROOT, "tools")

# Maya 에서 경로 문제 줄이기 위해 / 로 통일
TOOLS_ROOT = TOOLS_ROOT.replace("\\", "/")

# =========================
# MAYA SCRIPTS DIR
# =========================

maya_scripts_dir = os.path.join(
    "C:/Users",
    username,
    "Documents",
    "maya",
    "scripts"
)

maya_scripts_dir = maya_scripts_dir.replace("\\", "/")


# =========================
# CREATE DIR
# =========================

os.makedirs(maya_scripts_dir, exist_ok=True)


# =========================
# userSetup.py PATH
# =========================

user_setup_path = os.path.join(
    maya_scripts_dir,
    setupFile_name
)

user_setup_path = user_setup_path.replace("\\", "/")


# =========================
# userSetup.py CONTENT
# =========================

user_setup_code = f'''
import sys

TOOLS_ROOT = r"{TOOLS_ROOT}"

if TOOLS_ROOT not in sys.path:
    sys.path.append(TOOLS_ROOT)

print("JUN Tools Loaded")
'''

def get_unique_filepath(filepath):

    # 폴더 / 파일명 분리
    directory = os.path.dirname(filepath)

    filename = os.path.basename(filepath)

    # 확장자 분리
    name, ext = os.path.splitext(filename)

    # 원본 파일이 없으면 그대로 반환
    if not os.path.exists(filepath):
        return filepath

    # 001, 002...
    index = 1

    while True:

        new_filename = f"{name}_{index:03d}{ext}"

        new_filepath = os.path.join(
            directory,
            new_filename
        )

        if not os.path.exists(new_filepath):
            return new_filepath

        index += 1

# =========================
# WRITE FILE
# =========================

user_setup_path = get_unique_filepath(user_setup_path)

with open(user_setup_path, "w", encoding="utf-8") as f:
    f.write(user_setup_code)


# =========================
# DONE
# =========================

print("========================================")
print("userSetup.py created")
print(user_setup_path)
print("========================================\n")