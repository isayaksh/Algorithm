# 20915 숫자 카드 놀이
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  n = list(map(int,stdin.readline().rstrip()))
  N = []
  zero = 0 # 숫자 0 의 갯수
  for i in range(len(n)): # 숫자 6을 9로 변환
    if n[i] == 6:
      n[i] = 9
  for num in n: 
    if num == 0: # 숫자 0의 갯수 count
      zero += 1
    else: # 0 의외의 숫자 검열
      N.append(num)
  if len(n) == zero: # 모든 숫자의 값이 0일 경우
    print(0)
    continue
  N.sort(reverse=True) # 내림차순으로 정렬
  a = N[0]
  b = 0
  for i in range(1,len(N)):
    if a > b: # a의 값이 클 경우
      b = b * 10 + N[i]
    else: # b의 값이 클 경우
      a = a * 10 + N[i]
  for _ in range(zero):
    a *= 10
  print(a*b)