import os
import sys
import subprocess
import shutil

def build_exe():
    print("CSV to XLSX 변환기 EXE 빌드 시작...")
    
    # PyInstaller 명령어
    cmd = [
        "pyinstaller",
        "--onefile",                    # 단일 exe 파일 생성
        "--windowed",                   # 콘솔 창 숨기기
        "--name=CSV_to_XLSX_Converter", # exe 파일명
        "--icon=icon.ico",              # 아이콘 (선택사항)
        "--add-data=icon.ico;.",        # 아이콘 파일 포함
        "--hidden-import=pandas",
        "--hidden-import=openpyxl",
        "--hidden-import=chardet",
        "--hidden-import=tkinter",
        "csv_to_xlsx_converter.py"
    ]
    
    try:
        # PyInstaller 실행
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("빌드 성공!")
        print(f"EXE 파일 위치: dist/CSV_to_XLSX_Converter.exe")
        
        # dist 폴더의 exe 파일을 현재 디렉토리로 복사
        if os.path.exists("dist/CSV_to_XLSX_Converter.exe"):
            shutil.copy2("dist/CSV_to_XLSX_Converter.exe", ".")
            print("EXE 파일을 현재 폴더로 복사했습니다.")
            
    except subprocess.CalledProcessError as e:
        print(f"빌드 실패: {e}")
        print(f"오류 출력: {e.stderr}")
        return False
    
    # 임시 파일들 정리
    cleanup_folders = ["build", "__pycache__"]
    for folder in cleanup_folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"{folder} 폴더 삭제됨")
    
    # spec 파일 삭제
    spec_file = "CSV_to_XLSX_Converter.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"{spec_file} 삭제됨")
    
    return True

if __name__ == "__main__":
    success = build_exe()
    if success:
        print("\n✅ 빌드 완료! CSV_to_XLSX_Converter.exe 파일을 실행하세요.")
    else:
        print("\n❌ 빌드 실패!")
    
    input("Press Enter to exit...")
