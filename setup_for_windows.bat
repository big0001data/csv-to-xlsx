@echo off
echo CSV to XLSX 변환기 설치 및 빌드 스크립트
echo ==========================================

echo.
echo 1. Python 버전 확인...
python --version
if %errorlevel% neq 0 (
    echo Python이 설치되지 않았거나 PATH에 추가되지 않았습니다.
    echo https://python.org에서 Python을 다운로드하여 설치하세요.
    pause
    exit /b 1
)

echo.
echo 2. 필요한 라이브러리 설치...
pip install -r requirements.txt

echo.
echo 3. EXE 파일 빌드...
python build_exe.py

echo.
echo 빌드 완료!
pause
