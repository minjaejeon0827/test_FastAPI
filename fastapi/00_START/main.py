# AI 도구 fastapi 관련 질문
# 참고: https://gemini.google.com/app/8b1fe07309a58049?hl=ko

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

# Windows PowerShell 명령어
# 주의사항
# "curl --version" Windows PowerShell 명령어 실행시 오류는 발생하지만
# curl https://www.naver.com curl 명령어는 정상적으로 실행된다.        
# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.

# 새로운 기능 및 개선 사항에 대 한 최신 PowerShell을 설치 하세요! https://aka.ms/PSWindows

# PS C:\Users\NT371B5A> curl

# cmdlet Invoke-WebRequest(명령 파이프라인 위치 1)
# 다음 매개 변수에 대한 값을 제공하십시오.
# Uri: exit
# curl : 원격 이름을 확인할 수 없습니다.: 'exit'
# 위치 줄:1 문자:1
# + curl
# + ~~~~
#     + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-
#    WebRequest], WebException
#     + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWeb
#    RequestCommand

# PS C:\Users\NT371B5A> curl --version
# curl : 원격 이름을 확인할 수 없습니다.: '--version'
# 위치 줄:1 문자:1
# + curl --version
# + ~~~~~~~~~~~~~~
#     + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-
#    WebRequest], WebException
#     + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWeb
#    RequestCommand

# PS C:\Users\NT371B5A> curl https://www.naver.com

# 보안 경고: 스크립트 실행 위험
# Invoke-WebRequest는 웹 페이지의 내용을 구문 분석합니다. 페이지를 구문 분석할 때 웹 페이지 내
# 스크립트 코드가 실행될 수 있습니다.
#       권장 조치:
#       -UseBasicParsing 스위치를 사용하여 스크립트 코드 실행을 방지합니다.

#       계속하시겠어요?

# [Y] 예(Y)  [A] 모두 예(A)  [N] 아니요(N)  [L] 모두 아니요(L)  [S] 일시 중단(S)  [?] 도움말
# (기본값은 "N"):A


# StatusCode        : 200
# StatusDescription : OK
# Content           :    <!doctype html> <html lang="ko" class="fzoom"> <head> <meta charset="utf-8">
#                     <meta name="Referrer" content="origin"> <meta http-equiv="X-UA-Compatible" conte
#                     nt="IE=edge"> <meta name="viewport" cont...
# RawContent        : HTTP/1.1 200 OK
#                     transfer-encoding: chunked
#                     pragma: no-cache
#                     x-frame-options: DENY
#                     x-xss-protection: 1; mode=block
#                     strict-transport-security: max-age=63072000; includeSubdomains
#                     referrer-policy: ...
# Forms             : {sform}
# Headers           : {[transfer-encoding, chunked], [pragma, no-cache], [x-frame-options, DENY], [x-x
#                     ss-protection, 1; mode=block]...}
# Images            : {@{innerHTML=; innerText=; outerHTML=<img width="58" height="58" alt="NAVER" src
#                     ="https://s.pstatic.net/static/www/mobile/edit/20230516_0/upload_1684217675277OZ
#                     zsu.gif">; outerText=; tagName=IMG; width=58; height=58; alt=NAVER; src=https://
#                     s.pstatic.net/static/www/mobile/edit/20230516_0/upload_1684217675277OZzsu.gif},
#                     @{innerHTML=; innerText=; outerHTML=<img height="20" class="news_logo" alt="시사
#                     IN" src="https://s.pstatic.net/static/newsstand/up/2025/0418/nsd174916541.png">;
#                      outerText=; tagName=IMG; height=20; class=news_logo; alt=시사IN; src=https://s.
#                     pstatic.net/static/newsstand/up/2025/0418/nsd174916541.png}, @{innerHTML=; inner
#                     Text=; outerHTML=<img height="20" class="news_logo" alt="한국경제" src="https://
#                     s.pstatic.net/static/newsstand/up/2025/0418/nsd182845526.png">; outerText=; tagN
#                     ame=IMG; height=20; class=news_logo; alt=한국경제; src=https://s.pstatic.net/sta
#                     tic/newsstand/up/2025/0418/nsd182845526.png}, @{innerHTML=; innerText=; outerHTM
#                     L=<img height="20" class="news_logo" alt="블로터" src="https://s.pstatic.net/sta
#                     tic/newsstand/up/2025/0418/nsd17435516.png">; outerText=; tagName=IMG; height=20
#                     ; class=news_logo; alt=블로터; src=https://s.pstatic.net/static/newsstand/up/202
#                     5/0418/nsd17435516.png}...}
# InputFields       : {@{innerHTML=; innerText=; outerHTML=<input name="where" type="hidden" value="ne
#                     xearch">; outerText=; tagName=INPUT; name=where; type=hidden; value=nexearch}, @
#                     {innerHTML=; innerText=; outerHTML=<input name="sm" id="sm" type="hidden" value=
#                     "top_hty">; outerText=; tagName=INPUT; name=sm; id=sm; type=hidden; value=top_ht
#                     y}, @{innerHTML=; innerText=; outerHTML=<input name="fbm" id="fbm" type="hidden"
#                      value="0">; outerText=; tagName=INPUT; name=fbm; id=fbm; type=hidden; value=0},
#                      @{innerHTML=; innerText=; outerHTML=<input name="acr" disabled="disabled" id="a
#                     cr" type="hidden" value="">; outerText=; tagName=INPUT; name=acr; disabled=disab
#                     led; id=acr; type=hidden; value=}...}
# Links             : {@{innerHTML=<span>상단영역 바로가기</span>; innerText=상단영역 바로가기; outerH
#                     TML=<a href="#topAsideButton"><span>상단영역 바로가기</span></a>; outerText=상단
#                     영역 바로가기; tagName=A; href=#topAsideButton}, @{innerHTML=<span>서비스 메뉴
#                     바로가기</span>; innerText=서비스 메뉴 바로가기; outerHTML=<a href="#shortcutAre
#                     a"><span>서비스 메뉴 바로가기</span></a>; outerText=서비스 메뉴 바로가기; tagNam
#                     e=A; href=#shortcutArea}, @{innerHTML=<span>새소식 블록 바로가기</span>; innerTe
#                     xt=새소식 블록 바로가기; outerHTML=<a href="#newsstand"><span>새소식 블록 바로가
#                     기</span></a>; outerText=새소식 블록 바로가기; tagName=A; href=#newsstand}, @{in
#                     nerHTML=<span>쇼핑 블록 바로가기</span>; innerText=쇼핑 블록 바로가기; outerHTML
#                     =<a href="#shopping"><span>쇼핑 블록 바로가기</span></a>; outerText=쇼핑 블록 바
#                     로가기; tagName=A; href=#shopping}...}
# ParsedHtml        : mshtml.HTMLDocumentClass
# RawContentLength  : 253591



# PS C:\Users\NT371B5A>

# CMD 명령 프롬프트 curl 명령어 1
# 주의사항: Windows PowerShell 명령어와 달리 CMD 명령 프롬프트에서 "curl --version" 명령어 정상적으로 실행 된다.
# Microsoft Windows [Version 10.0.26100.8246]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\NT371B5A>curl --version
# curl 8.18.0 (Windows) libcurl/8.18.0 Schannel zlib/1.3.1 WinIDN WinLDAP
# Release-Date: 2026-01-07
# Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s smb smbs smtp smtps telnet tftp ws wss
# Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets

# C:\Users\NT371B5A>curl --version
# curl 8.18.0 (Windows) libcurl/8.18.0 Schannel zlib/1.3.1 WinIDN WinLDAP
# Release-Date: 2026-01-07
# Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s smb smbs smtp smtps telnet tftp ws wss
# Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets

# C:\Users\NT371B5A>

# CMD 명령 프롬프트 curl 명령어 2
# 참고: https://gemini.google.com/app/8b1fe07309a58049?hl=ko
# 주의사항
# curl http://127.0.0.1:8000/items/?skip=1&limit=10 curl 명령어 실행 시 아래처럼 오류 발생하므로 curl 명령어 따옴표("") 추가 수정 해야함.
# (기존) curl http://127.0.0.1:8000/items/?skip=1&limit=10 -> (변경) curl "http://127.0.0.1:8000/items/?skip=1&limit=10"
# 오류 메시지: {"skip":"1","limit":10}'limit'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.
# Microsoft Windows [Version 10.0.26100.8246]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\NT371B5A>curl --version
# curl 8.18.0 (Windows) libcurl/8.18.0 Schannel zlib/1.3.1 WinIDN WinLDAP
# Release-Date: 2026-01-07
# Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s smb smbs smtp smtps telnet tftp ws wss
# Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets

# C:\Users\NT371B5A>curl --version
# curl 8.18.0 (Windows) libcurl/8.18.0 Schannel zlib/1.3.1 WinIDN WinLDAP
# Release-Date: 2026-01-07
# Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s smb smbs smtp smtps telnet tftp ws wss
# Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets

# C:\Users\NT371B5A>curl http://127.0.0.1:8000/
# {"message":"Hello, World!"}
# C:\Users\NT371B5A>curl http://127.0.0.1:8000/items/1
# {"item_id":"1"}
# C:\Users\NT371B5A>curl http://127.0.0.1:8000/items/\?skip\=1\&limit\=10
# {"item_id":"\\"}'limit\'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
# 배치 파일이 아닙니다.

# C:\Users\NT371B5A>curl http://127.0.0.1:8000/items/?skip=1&limit=10
# {"skip":"1","limit":10}'limit'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
# 배치 파일이 아닙니다.

# C:\Users\NT371B5A>curl "http://127.0.0.1:8000/items/?skip=1&limit=10"
# {"skip":"1","limit":"10"}
# C:\Users\NT371B5A>curl "http://127.0.0.1:8000/items/"
# {"skip":0,"limit":10}
# C:\Users\NT371B5A>