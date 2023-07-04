# BOJ 1446 지름길
# https://www.acmicpc.net/problem/1446

from sys import stdin
from collections import deque

def solution(N, D, edges):

    N = len(edges)
    answer = 10001
    edges.sort()

    queue = deque([(0, 0, 0)])
    while queue:
        node, weight, idx = queue.popleft()

        # 모든 지름길을 이용했을 경우
        if idx == N:
            answer = min(answer, weight + D - node)
            continue

        s, e, w = edges[idx] # 시작 위치, 도착 위치, 지름길의 길이

        # 현재 위치가 지름길의 시작 위치보다 뒤인 경우
        if node > s:
            queue.append((node, weight, idx+1))
        # 현재 위치가 지름길의 시작 위치보다 앞이거나 같은 경우
        else:
            queue.append((e, weight + w + (s - node), idx+1))
        
        # 지름길을 사용하지 않는 경우
        queue.append((node, weight, idx+1))
    
    return answer

N, D = map(int,stdin.readline().split())
edges = []
for _ in range(N):
    s, e, w = map(int,stdin.readline().split())
    if e <= D:
        edges.append((s, e, w))

res = solution(N, D, edges)
print(res)