# 리스트 계속

a = [1, 2, 3]
print(a)

# 자료구조 stack에 있는 pop기능 구현
print(a.pop()) # 리스트 맨 마지막 요소를 꺼냄
print(a)

a.append(10) # 3꺼내고 10 다시 집어넣은 상태
print(a)

print(a.count(3)) # 리스트안에 3이 몇개 있는지 셈 => 0

# 리스트 확장 a = 1, 2, 10
a.extend([5, 3, 2])
print(a) # [1, 2, 10, 5, 3, 2]
print(a.count(2)) # => 2
