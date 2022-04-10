# 1461 도서관 < 골드 5 >
from sys import stdin
N, M = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))
neg = [0] # 음수
pos = [0] # 양수
result = 0
for l in lst:
  if l < 0: neg.append(l) # 음수는 neg 배열에 추가
  else: pos.append(l) # 양수는 pos 배열에 추가
neg.sort(reverse=True) # 음수 내림차순 정렬
pos.sort() # 양수 오름차순 정렬
posLen = len(pos) # 양수의 갯수
negLen = len(neg) # 음수의 갯수
for i in range((posLen-1)%M, posLen, M):
  result += pos[i]*2
for i in range((negLen-1)%M, negLen, M):
  result += abs(neg[i])*2
result -= max(abs(neg[-1]),pos[-1])
print(result)