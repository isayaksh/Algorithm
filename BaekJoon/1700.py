# 1700 멀티탭 스케줄링 < 골드 1 >
from sys import stdin

Plug = [] # 현재 플러그에 꽂혀있는 전자기기의 정보
count = 0 # 콘센트를 뽑는 경우의 수
N, K = map(int,stdin.readline().split()) # 콘센트 수, 사용할 전자기기 개수
Order = list(map(int,stdin.readline().split())) # [ 사용할 전자기기 순서]

for i in range(K):
  if Order[i] in Plug: # 현재 멀티탭에 전기 용품이 꽂혀있을 경우
    continue
  if len(Plug) < N: # 멀티탭에 공간이 존재할 경우
    Plug.append(Order[i])
    continue
  # 현재 멀티탭에 공간이 없고 전기 용품이 꽂혀있지 않을 경우
  idx = 0 # 멀티탭에서 제거할 전기 용품의 위치
  MAX = 0 # 멀티탭에서 멀리 위치
  for j in range(N):
    try:
      if MAX < Order[i:].index(Plug[j]):
        MAX = Order[i:].index(Plug[j])
        idx = j
    except:
      idx = j
      break
  Plug[idx] = Order[i]
  count += 1
print(count)