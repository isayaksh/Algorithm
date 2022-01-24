# 14659 한조 서열정리하고옴ㅋㅋ <브론즈 2>
from sys import stdin
N = int(stdin.readline())
H = list(map(int,stdin.readline().split()))
result = [] # 결과값
tmp = 0 # 임시 값
for i in range(1,N):
  if H[i-1] < H[i]: # 현재의 봉우리가 현재 가장 큰 값보다 크다면
    result.append(tmp)
    tmp = 0
  else:
    H[i] = H[i-1]
    tmp += 1
result.append(tmp) # 만약 첫번째 원소가 가장 큰 값인 경우
print(max(result))