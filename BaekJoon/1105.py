# 1105 팔 < 실버 1 >
from sys import stdin
L, R = stdin.readline().rstrip().split()
num = len(R) - len(L)
count = 0
if num: # 입력받은 L, R의 길이가 다르다면
  print(0) # 0 출력 후
  exit() # 프로그램 종료
for i in range(len(L)):
  if L[i] != R[i]: # 현재 값이 다르다면
    break # 종료
  else: # 현재 값이 같은데
    if L[i] == '8': # 현재 값이 8이라면
      count += 1 # 8의 갯수 + 1
print(count)