# 2841 외계인의 기타 연주
from sys import stdin
N, P = map(int,stdin.readline().split())
D = [[] for _ in range(N+1)]
count = 0
for _ in range(N):
  L, F = map(int,stdin.readline().split())
  if D[L]:
    while D[L][-1] > F: # L 줄의 F 플랫보다 높은 플랫에 손가락이 존재한다면
      D[L].pop() # 운지한 손가락 제거
      count += 1 # 손가락 움직임 + 1
      if not D[L]: # 만약 L줄에 운지한 손가락이 없다면
        break # 반복문 종료
  if D[L] and (D[L][-1] == F): # 만약 F플랫과 L번째 줄의 마지막 플랫이 같다면
    continue # 다음 반복문 실행
  D[L].append(F) # L 줄에 F 플랫 추가
  count += 1 # 손가락 움직임 + 1
print(count)