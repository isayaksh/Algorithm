# 9935 문자열 폭발 < 골드 4 >
from collections import deque
from sys import stdin
F = []
B = deque(list(stdin.readline().rstrip()))
word = stdin.readline().rstrip()
length = len(word)
while B:
  F.append(B.popleft()) # 입력받은 문자열의 앞에서 문자를 한개씩 입력 
  if F[-1] == word[-1]: 
    if "".join(F[-length:]) == word: # 현재 문자열의 마지막 부분이 word와 같다면
      for _ in range(length): # word 길이만큼
        F.pop() # 현재 문자열에서 제거
if F:
  print("".join(F))
else:
  print("FRULA")