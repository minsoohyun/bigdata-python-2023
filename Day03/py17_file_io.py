# 파일 입출력
# DB open / close   Network open / close   File open / close
import os 

cur_path = os.getcwd() # 현재 파이썬 경로(많이 사용)
print(cur_path)
filename='./Day03/sample.txt' #상대경로
# filename='C:\\Source\\bigdata-python-2023\\Day03\\test.txt' # 절대경로
# filename='C:/Source/bigdata-python-2023/Day03/test2.txt' # 절대경로 리눅스/유닉스와 동일하게 사용가능
f = open(filename, mode='wt', encoding='utf-8') # 텍스트 파일 생성(ascii코드 기본)

f.write('한국어\n')
f.write('인생은 아름다워!!') # 마지막 문장에는 \n을 안쓰는게 좋음

f.close() # 무조건 닫아줘야함
print(f'{filename} 파일이(가) 생성되었습니다')

fr = open(filename, mode='rt', encoding='utf-8')
while True: #무한루프
    line = fr.readline() # 한 줄씩 읽기
    if not line: break   # 읽을 줄이 없으면 빠져나감
    print(line, end='')  # \n과 엔터가 두 번 들어감

fr.close() #파일 닫기 반드시!

