# 13417 카드 문자열 < 실버 3 >
from sys import stdin
from collections import deque
T = int(stdin.readline())
for _ in range(T):
  N = int(stdin.readline())
  word = list(stdin.readline().rstrip().split())
  result = deque(word[0]) # 결과 값을 저장할 deque
  for i in range(1,N):
    if result[0] >= word[i]: # 사전순으로 맨 앞의 글자와 같거나 작으면
      result.appendleft(word[i]) # 왼쪽에 추가
    else: # 사전순으로 맨 앞의 글자보다 크면
      result.append(word[i])  # 오른쪽에 추가
  print(''.join(result))