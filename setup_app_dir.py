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

# setUp_app_dir.py 가 있는 폴더 경로
TOOLS_ROOT = os.path.dirname(os.path.abspath(__file__))
TOOLS_ROOT = os.path.join(TOOLS_ROOT, "/tools")

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


# =========================
# WRITE FILE
# =========================

with open(user_setup_path, "w", encoding="utf-8") as f:
    f.write(user_setup_code)


# =========================
# DONE
# =========================

print("========================================")
print("userSetup.py created")
print(user_setup_path)
print("========================================")