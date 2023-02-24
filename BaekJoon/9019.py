# BOJ 9019 DSLR
# https://www.acmicpc.net/problem/9019

from sys import stdin
from collections import deque

def bfs(A, B, order):
    queue = deque([(A, '')])
    visited = [False] * 10000
    visited[A] = True
    while queue:
        A, order = queue.popleft()
        
        if A == B:
            return order
        
        D = (A * 2) % 10000
        if not visited[D]:
            queue.append((D, order +'D'))
            visited[D] = True
        
        S = (A - 1) % 10000
        if not visited[S]:
            queue.append((S, order + 'S'))
            visited[S] = True

        L = (A % 1000) * 10 + (A // 1000)
        if not visited[L]:
            queue.append((L, order + 'L'))
            visited[L] = True
        
        R = (A % 10) * 1000 + (A // 10)
        if not visited[R]:
            queue.append((R, order + 'R'))
            visited[R] = True

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int,stdin.readline().split())
    print(bfs(A, B, ''))