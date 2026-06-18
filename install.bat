@echo off
REM ============================================================
REM  Maya Tool Release - one-file installer / updater
REM  - 빈 폴더에 이 파일 하나만 두고 실행하면 저장소를 git clone 한다.
REM  - 이미 받아둔 저장소(또는 그 안)에서 실행하면 최신으로 업데이트한다.
REM  - 끝으로 Maya scripts/userSetup.py 에 tools 경로를 등록한다.
REM ============================================================

setlocal
cd /d %~dp0

set "REPO_URL=https://github.com/elom1213/Maya_Tool_Release.git"
set "REPO_DIR=Maya_Tool_Release"

REM --- 요건 확인: git -----------------------------------------
where git >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Git is not installed or not on PATH.
    echo         Install Git first: https://git-scm.com/
    pause
    exit /b 1
)

REM --- 요건 확인: python launcher 'py' -----------------------
where py >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python launcher 'py' not found.
    echo         Install Python 3: https://www.python.org/
    pause
    exit /b 1
)

REM --- Case 1: 이미 저장소 안에서 실행 -> 제자리 업데이트 -----
if exist ".git" (
    echo Repository detected here. Updating in place...
    goto :run_setup
)

REM --- Case 2: 하위에 이미 clone 되어 있음 -> 그 안에서 갱신 --
if exist "%REPO_DIR%\.git" (
    echo Existing clone found. Updating...
    cd /d "%~dp0%REPO_DIR%"
    goto :run_setup
)

REM --- Case 3: 처음 -> clone ---------------------------------
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
py update.py
py setup_app_dir.py
echo.
echo ========================================
echo Install / Update Complete
echo ========================================
pause
exit /b 0
