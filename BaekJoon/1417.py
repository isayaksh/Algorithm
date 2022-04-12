# 1417 국회의원 선거 <실버 5>
from sys import stdin
N = int(stdin.readline())
DS = int(stdin.readline()) # 현재 다솜이의 득표 수
if N == 1: # 국회의원 선거에 다솜이가 유일하다면
  print(0)
  exit()
result = 0
lst = []
for _ in range(N-1):
  lst.append(int(stdin.readline()))
while(1):
  lst.sort(reverse=True) # 내림차순으로 정렬
  if DS > lst[0]: # 현재 다솜이의 득표 수가 가장 높다면
    break # 종료
  DS += 1 # 다솜이의 득표 수 + 1
  result += 1 # 매수 인구 + 1
  lst[0]-=1 # 타 국회의원 득표 수 - 1
print(result)