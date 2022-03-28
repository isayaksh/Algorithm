# 14247 나무 자르기
from sys import stdin
n = int(stdin.readline())
H = list(map(int,stdin.readline().split()))
A = list(map(int,stdin.readline().split()))
lst = []
result = 0
for i in range(n):
  lst.append([A[i],H[i]]) # [ 성장 길이, 초기 높이]
lst.sort() # 성장 길이 기준으로 정렬
for i in range(n-1,-1,-1):
  a = lst[i][0] # 성장 길이
  h = lst[i][1] # 초기 높이
  result += (h + (a * i)) # 초기 높이 + 성장 길이 * 성장 기간
print(result)