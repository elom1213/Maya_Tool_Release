@echo off

cd /d %~dp0

echo Updating Tools...

py update.py
py setup_app_dir.py

pause