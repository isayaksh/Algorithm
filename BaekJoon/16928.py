# BOJ 16928 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928

from sys import stdin
from collections import deque

def solution(path):

    pathSet = set(s for s in path)

    visited = [False] * 101
    visited[1] = True    

    queue = deque([(1, 0)])
    while queue:
        pos, cnt = queue.popleft()
        if pos == 100:
            return cnt
        for move in range(1, 7):
            nextPos = pos + move
            if nextPos < 101 and not visited[nextPos]:
                while nextPos in pathSet:
                    nextPos = path[nextPos]
                visited[nextPos] = True
                queue.append((nextPos, cnt+1))
                

N, M = map(int,stdin.readline().split())
path = dict()

for _ in range(N+M):
    s, e = map(int,stdin.readline().split())
    path[s] = e

res = solution(path)
print(res)