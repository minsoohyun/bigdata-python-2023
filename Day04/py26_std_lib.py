# 표준 라이브러리
# import datetime as dt
from datetime import date, datetime

first_date = date(2022, 12, 25)
print(first_date)
cur_date = date.today()
print(cur_date-first_date)

cur_dt = datetime.now() #많이 씀
print(cur_dt)
print(cur_dt.strftime('%Y-%m-%d')) # date.today()와 동일하지만 str타입

print(cur_dt.weekday()) #월요일이 0부터
print(cur_dt.isoweekday()) #월요일이 1부터

import time

for x in range(10):
    print(x)
    # time.sleep(0.1) # second C#,java, C++ time.slepp(ms)

import math
print(math.pi) #pi모듈

import os
# print(os.environ)
# print(os.environ['PATH'])
# print(os.getcwd()) #지금 실행중인 위치
print(os.system('dir')) 
print(os.system('git --version')) #콘솔 명령어 실행

import json

with open('./Day04/data.json',mode='r',encoding='utf-8') as f:
    data = json.load(f) # load => str / loads => byteArray
print(data)

## urllib
from urllib.request import urlopen

res = urlopen('https://www.naver.com')
print(res.status) # 200 OK
print(res.read().decode('utf-8')) # index.html 가져옴 => 웹 크롤링

import webbrowser
webbrowser.open('https://www.naver.com')

