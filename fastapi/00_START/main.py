# fastapi 터미널 설치 명령어(Python 3.6 이상 필요.)
# pip install fastapi
# pip install fastapi==0.104.1(파이썬 동영상 강의 실습 환경)

# uvicorn 터미널 설치 명령어
# pip install uvicorn
# pip install uvicorn==0.27.0.post1(파이썬 동영상 강의 실습 환경)

# fastapi 웹서버 터미널 실행 명령어
# 실습: uvicorn 00_START.main:app --reload
# 기본: uvicorn main:app --reload
# uvicorn main: - main.py 소스파일
# app: FastAPI 인스턴스 app 실행
# --reload: FastAPI 인스턴스 app 실행한 후에 
# 예를들어 return {"message": "Hello, World!"} 소스 코드 수정해서 
# 다시 main.py 소스파일 저장하면 해당 웹서버 프로그램을 종료했다가 
# 다시 실행할 필요 없이 바로 소스 코드 수정사항 반영해준다.

# FastAPI 버전 확인 터미널 명령어
# pip show fastapi

# 소스코드
# 참고: https://gist.github.com/DaveLee-fun/e04635abeb0af52c431090e80fed7e04

from fastapi import FastAPI  # FastAPI 클래스 가져옴.

app = FastAPI()  # FastAPI 인스턴스 생성

@app.get("/")  # HTTP GET 요청 경로 지정
def read_root():  # GET 요청 처리 함수
    return {"message": "Hello, World!"}  # JSON 형태 응답 반환(구글 크롬 웹브라우저). FastAPI가 자동 변환

# FastAPI 웹서버 실행하여 아래 오류 메시지 출력시 해결 방법
# 방법 1. 실습: uvicorn 00_START.main:app --reload 명령어 실행
# 방법 2. 해당 폴더로 직접 들어가서 실행
# 1) main.py 파일이 들어있는 방(폴더)으로 들어간 뒤에 실행하는 방법
# 2) 터미널에 폴더 이동 명령어 입력: cd 00_START
# 3) 그 다음 기존 명령어 입력: uvicorn main:app --reload
# 참고: https://gemini.google.com/app/8b1fe07309a58049?hl=ko
# (fastapi_env) PS D:\minjae\test_FastAPI\fastapi> uvicorn main:app --reload
# INFO:     Will watch for changes in these directories: ['D:\\minjae\\test_FastAPI\\fastapi']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [720] using StatReload
# ERROR:    Error loading ASGI app. Could not import module "main".
# WARNING:  StatReload detected changes in '00_START\main.py'. Reloading...
# ERROR:    Error loading ASGI app. Could not import module "main".
# WARNING:  StatReload detected changes in '00_START\main.py'. Reloading...
# ERROR:    Error loading ASGI app. Could not import module "main".
# WARNING:  StatReload detected changes in '00_START\main.py'. Reloading...
# ERROR:    Error loading ASGI app. Could not import module "main".
# WARNING:  StatReload detected changes in '00_START\main.py'. Reloading...
# ERROR:    Error loading ASGI app. Could not import module "main".
# WARNING:  StatReload detected changes in '00_START\main.py'. Reloading...
# ERROR:    Error loading ASGI app. Could not import module "main".

