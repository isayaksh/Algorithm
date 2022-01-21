# 3135 라디오
from sys import stdin

A, B = map(int, stdin.readline().split())
N = int(stdin.readline())
F = []
for _ in range(N):
  F.append(int(stdin.readline()))

# 현재 주파수 - 듣고싶은 주파수의 절대값
result = abs(A - B)
# 즐겨찾기 주파수로 이동하는지 안하는지 여부
TF = False

for f in F:
  # 듣고싶은 주파수 - 즐겨찾기 주파수의 절대 값이 result보다 작다면
  if result > abs(B - f):
    result = abs(B - f) # result = 듣고싶은 주파수 - 즐겨찾기 주파수의 절대 값
    TF = True # 즐겨찾기 주파수 사용시 True
if TF: # 즐겨찾기 주파수를 사용했다면
  print(result+1) 
else: # 즐겨찾기 주파수를 사용하지 않았다면
  print(result)