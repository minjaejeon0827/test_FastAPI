# fastapi 코드잇 최종 프로젝트 소스코드(2026.04.16 minjae)
# 참고: https://github.com/gyurili/2025-GEO-Project.git

# pymysql - Pymysql을 사용하여 Python과 SQL 연동하기
# 참고: https://youtu.be/XVJ4yRaqb-w?si=dDfXm3AdLuBq1wU4

# pymysql - DB 프로그래밍1 - 파이썬 세팅 및 주소록 프로그램 제작
# 참고: https://youtu.be/MLNFyBAHvq0?si=xd8rOxg2sfVhtKtn

# pymysql - DB 프로그래밍2 - pymysql로 db연동
# 참고: https://youtu.be/R3SSNTE2CQE?si=9jLbmFRQ9XEo6PBZ

# pymysql - [SQL 기초 강의] 22강. 파이썬과 MySQL 연동하기
# 참고: https://youtu.be/Se1ImwcqmlA?si=_F5ItimSCr51Nvbb

# pymysql - Python: MySQL과 파이썬 연동하기 (pymysql)
# 참고: https://youtu.be/B956r7XzJIA?si=kKRhZ3-w2ykHhUuB


# fastapi MySQL CRUD 연동 유튜브 동영상
# 참고: https://youtu.be/7frN5JPMsQU?si=8EXm2RaSLKuer5p1
# 참고 2: https://youtu.be/ooHWO2gP7Qo?si=5dZA7BMKllqe70mT
# 참고 3: https://youtu.be/S-XvcwNcYp4?si=RDt4yrshUq5JlQjE
# 참고 4: https://youtu.be/N8i4GcRRkV8?si=x8ySwLj2MDFmdyu6
# 참고 5: https://youtu.be/5dqKuNhkkjA?si=WPapYU-t44maMX65
# 참고 6: https://youtu.be/4KljjdbcWJ0?si=BLkcYfPv9SQpswuX
# 참고 7: https://youtu.be/aoPGAoPjF3I?si=eaSZZUNaX_7Hs8Gi

# Ubuntu 리눅스 사용 방법
# Visual Studio Code를 윈도우 WSL환경과 함께 이용해보자.
# 참고: https://www.youtube.com/live/s_Tt_C_X0ZI?si=rzpnpWUvRKJ_Ci9X

# GIT 커밋 메시지 작성 방법
# 참고: https://wikidocs.net/332862

# fastapi 터미널 설치 명령어(Python 3.6 이상 필요.)
# pip install fastapi
# pip install fastapi==0.104.1(파이썬 동영상 강의 실습 환경)

# uvicorn 터미널 설치 명령어
# pip install uvicorn
# pip install uvicorn==0.27.0.post1(파이썬 동영상 강의 실습 환경)

# fastapi 웹서버 터미널 실행 명령어
# 실습: uvicorn 00_START.main:app --reload
# 기본: uvicorn main:app --reload
# main: FastAPI 애플리케이션 코드가 있는 Python 파일명 (main.py)
# app: FastAPI 인스턴스 객체명(app = FastAPI())
# --reload: 개발 중 코드 변경 시 자동으로 서버 재시작
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

# URL 1 - http://127.0.0.1:8000/ 
# URL 2 - http://127.0.0.1:8000 둘 다 동일.
@app.get("/")  # HTTP GET 요청 경로 지정
def read_root():  # GET 요청 처리 함수
    return {"message": "Hello, World!"}  # JSON 형태 응답 반환(구글 크롬 웹브라우저). FastAPI가 자동 변환

# URL - http://127.0.0.1:8000/hello
@app.get("/hello")  # HTTP GET 요청 경로 지정
def read_hi():  # GET 요청 처리 함수
    return {"message": "Hi, World!"}  # JSON 형태 응답 반환(구글 크롬 웹브라우저). FastAPI가 자동 변환

# 1. 경로 매개변수 (Path Parameters)
# 첫 번째 코드는 주소 자체에 핵심 정보를 쏙 끼워 넣는 방식이에요. 
# 마치 "아파트 101동 502호로 배달해 주세요"라고 정확한 위치를 콕 집어 말하는 것과 같아요.
# URL - http://127.0.0.1:8000/items/1
# 클라이언트(사용자)가 웹 브라우저 주소창에 http://127.0.0.1:8000/items/1 이라고 접속했을 때 실행됩니다.
@app.get("/items/{item_id}")  # HTTP GET 요청 경로 지정 - 경로 매개변수(Path Parameters)
def read_item(item_id):  # GET 요청 처리 함수 - 방금 위 주소의 {item_id} 빈칸에 들어온 숫자를 그대로 가져와서 'item_id'라는 이름표를 붙여줍니다.
    return {"item_id": item_id}  # JSON 형태 응답 반환(구글 크롬 웹브라우저). FastAPI가 자동 변환  

# 2. 쿼리 매개변수 (Query Parameters)
# 두 번째 코드는 기본 주소 뒤에 물음표(?)를 붙여서 **추가적인 옵션(조건)**을 달아주는 방식이에요.
# 식당에서 "떡볶이 하나 주시는데, 맵기는 중간으로, 치즈 추가해서요"라고 옵션을 말하는 것과 완벽히 똑같아요.
# URL - http://127.0.0.1:8000/items/?skip=5&limit=5
# URL(default) - http://127.0.0.1:8000/items/
# 주소창에 http://127.0.0.1:8000/items/?skip=5&limit=5 라고 입력했을 때 실행됩니다.
@app.get("/items/")  # HTTP GET 요청 경로 지정 - 쿼리 매개변수(Query Parameters)
def read_items(skip = 0, limit = 10):  # GET 요청 처리 함수
    # 여기가 핵심이에요! 주소 끝에 물음표(?)를 붙이고 추가로 적은 옵션 값들을 여기서 받아요.
    # - 주소창에 ?skip=5 라고 적었으면, 컴퓨터는 "아, skip 값을 5로 하라는 뜻이구나!" 하고 알아듣습니다.
    # - 만약 아무 옵션도 없이 그냥 /items/ 로 접속하면? 컴퓨터가 당황하지 않게 "그럼 skip은 0, limit는 10으로 기본값을 정해둘게"라고 안전장치(=0, =10)를 마련해 둔 거예요.
    return {"skip": skip, "limit": limit}  # JSON 형태 응답 반환(구글 크롬 웹브라우저). FastAPI가 자동 변환

# 💡 핵심 요약 비교
# 경로 매개변수 (/items/1): 찾고자 하는 대상의 고유한 번호나 정확한 위치를 나타낼 때 써요. (예: 1번 회원 정보, 5번 게시물)

# 쿼리 매개변수 (/items/?skip=5&limit=5): 정렬, 필터링, 페이지 나누기 등 추가적인 옵션을 줄 때 써요. 물음표 뒤에 이름=값 형태로 길게 이어 붙일 수 있어요.

# 코드가 어떻게 작동하는지 머릿속에 그림이 조금 그려지셨나요? 천천히 읽어보시고 이 과정을 완벽하게 내 것으로 만들어보세요!


# Swagger UI URL - http://127.0.0.1:8000/docs
# ReDoc UI URL - http://127.0.0.1:8000/redoc

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

