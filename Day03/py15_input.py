# 입출력
import datetime # 날짜 모듈 가져옴

# birth_year = int(input('출생년도를 입력하세요 > ')) # 키보드 입력(string타입 => int로 형변환)

# print(f'당신의 출생년도는 {birth_year}년 입니다.') # 콘솔출력
# curr_year = datetime.datetime.now().year # {}는 모듈을 뜻함
# age = curr_year - birth_year
# print(f'당신의 나이는 {age}세 입니다.')

a = 123
a = [3, 6, 9]
print(a)

print("life" "is" "too short")
print("life"+"is"+"too short")
print("life","is","too short") # 콤마로 구분하면 공백으로 나옴
print("life", 3.141592, True)

print(range(10))
print(len(range(10)))

for i in range(10):
    if i == (len(range(10)) - 1):
        print(i, end = '\n') #마지막자리에서 줄바꿈
    else:
        print(i, end=', ')

print('life', 'is', 'too short', sep='#') #콤마 사이에 입력한 문자로 구분해줌. 잘안씀

pi = 3.141592

print(f'PI = {pi:.4f}') # 네 번째 자리에서 반올림돼서 나옴
print(f'PI = {pi:10.2f}')