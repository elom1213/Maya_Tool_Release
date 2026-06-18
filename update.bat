@echo off

cd /d %~dp0

echo Updating Tools...

py scripts\update.py
py scripts\setup_app_dir.py

pause