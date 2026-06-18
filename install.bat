@echo off
REM ============================================================
REM  Maya Tool Release - one-file installer / updater
REM  - Run this single file in an empty folder: it git-clones the repo.
REM  - Run it again (or inside an existing clone): it updates to latest.
REM  - Then it registers the tools path into Maya scripts/userSetup.py.
REM  NOTE: keep this file ASCII + CRLF so cmd parses it on any locale.
REM ============================================================

setlocal
cd /d %~dp0

set "REPO_URL=https://github.com/elom1213/Maya_Tool_Release.git"
set "REPO_DIR=Maya_Tool_Release"

REM --- requirement: git ---------------------------------------
where git >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Git is not installed or not on PATH.
    echo         Install Git first: https://git-scm.com/
    pause
    exit /b 1
)

REM --- requirement: python launcher 'py' ----------------------
where py >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python launcher 'py' not found.
    echo         Install Python 3: https://www.python.org/
    pause
    exit /b 1
)

REM --- Case 1: already inside the repo -> update in place ------
if exist ".git" (
    echo Repository detected here. Updating in place...
    goto :run_setup
)

REM --- Case 2: a clone already exists below -> update it -------
if exist "%REPO_DIR%\.git" (
    echo Existing clone found. Updating...
    cd /d "%~dp0%REPO_DIR%"
    goto :run_setup
)

REM --- Case 3: first run -> clone -----------------------------
echo Cloning %REPO_URL% ...
git clone "%REPO_URL%" "%REPO_DIR%"
if errorlevel 1 (
    echo [ERROR] git clone failed. Check your network and repo access.
    pause
    exit /b 1
)
cd /d "%~dp0%REPO_DIR%"

:run_setup
echo.
py scripts\update.py
py scripts\setup_app_dir.py
echo.
echo ========================================
echo Install / Update Complete
echo ========================================
pause
exit /b 0
