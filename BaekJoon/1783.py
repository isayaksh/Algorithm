# 1783 병든 나이트 < 실버 4 >
from sys import stdin
N, M = map(int,stdin.readline().split()) # 세로, 가로
if N == 1: # 세로 길이가 1일 경우
  count = 1 # 경우 없이 모두 1
elif N == 2: # 세로 길이가 2일 경우
  if M <= 7: count  = (M+1)//2 # 가로가 7보다 작을 경우 (M+1)//2
  else: count = 4 # 나머지 모든 경우 4
elif 3 <= N: # 세로 길이가 3이상일 경우
  if M <= 4: count = M # 가로가 4보다 작은 경우 M
  elif 5 <= M <= 6: count = 4 # 5~6의 경우 4
  else: count = M - 2 # 나머지 모든 경우 M - 2
print(count)