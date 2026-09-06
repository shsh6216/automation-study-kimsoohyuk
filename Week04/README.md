## 1. 실행환경 준비 방법
가상환경을 생성하고 실행합니다.
python -m venv venv
.\venv\Scripts\Activate.ps1

## 2. 필요한 라이브러리 설치
pip install -r requirements.txt

## 3. 환경설정 준비 방법
`.env.example` 파일을 참고하여 `.env` 파일을 생성합니다.
ID = 로그인 ID
PASSWORD = 로그인 Password
URL = 기본 접속 URL
MEMO = 입력한 메모가 저장되는 파일

## 4. 프로그램 실행 방법
터미널에서 py memo_v2.py 명령어를 통해 테스트를 실행할 수 있습니다.
메모를 입력하면 MEMO에 설정한 파일에 메모가 저장됩니다.
MEMO 설정이 없는 경우 기본값인 memos.json에 저장됩니다.