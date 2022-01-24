# 2810 컵홀더 <브론즈 2>
from sys import stdin

N = int(stdin.readline())
S = list(stdin.readline().rstrip())
C = 1 # 컵홀더
i = 0 #  index
while i < N:
  if S[i] == 'L': # 커플석일 경우
    i+=2 # index 2 증가
  else: # 커플석이 아닐 경우
    i+=2 # index 1 증가
  C+=1 # 컵홀더 1 증가
print(min(C,N))