# 2493 탑 <골드 5>
from sys import stdin

N = int(stdin.readline())
T = [0]+list(map(int,stdin.readline().split()))

result = ["0" for _ in range(N+1)]
D = [] 

for i in range(1,N+1):
  if T[i-1] > T[i]: # 바로 왼쪽의 타워가 현재 타워보다 높으면
    result[i] = str(i-1) # 왼쪽 타워의 인덱스 입력
  else: # 바로 왼쪽의 타워가 현재 타워보다 낮으면
    while D and T[D[-1]] < T[i]: # 현재타워가 앞선 타워들 보다 낮을 때 까지
      D.pop() # 앞선 타워들 제거
    if D: # 현재 타워보다 높은 타워가 있으면
      result[i] = str(D[-1]) # 높은 타워의 인덱스 입력
  D.append(i) # 현재 타워를 추가

print(" ".join(result[1:]))