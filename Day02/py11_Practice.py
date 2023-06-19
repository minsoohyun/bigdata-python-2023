# Q1
d1 = {'국어' : 80,
      '영어' : 75,
      '수학' : 55}
# print(d1)
sum = sum(d1.values())
print(sum)
average = sum / len(d1)
print(f'평균 : {average }')


# Q2
a = 13
b = a % 2 == 0
print(f'{a}는 짝수? {b}')

# Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
# yyyymmdd = pin.split('-')[0]
# num = pin.split('-')[1]

print(yyyymmdd)
print(num)

# Q6
a = [1,3,5,4,2]
a.sort()
a.reverse() #a.sort(reverse=True)와 같음
print(a)

# Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)   # 리스트를 집합으로 변환해서 중복제거
b = list(aSet)  # 다시 리스트로 변환
print(b)