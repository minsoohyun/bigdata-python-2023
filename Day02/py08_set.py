# 집합 => 중복된거는 안나옴
s1 = set([1,2,3,4,5,1,2,3])
print(s1)

s2 = set((3,6,9,12,3,12,15))
print(s2)

s3 = set('Hello')
print(s3)

print(list(s3))  # 집합을 리스트로 변경(가장 많은 빈도로 사용)
print(tuple(s3)) # 집합을 튜플로 변경
