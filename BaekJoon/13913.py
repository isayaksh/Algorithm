# BOJ 13913 숨바꼭질 4
# https://www.acmicpc.net/problem/13913

from sys import stdin, maxsize
from collections import deque

def solution(N, K):
    graph = [[maxsize, -1] for _ in range(100001)]
    graph[N] = [0, N]

    queue = deque([N])
    while queue:
        node = queue.popleft()
        if node*2 < 100001 and graph[node][0] + 1 < graph[node*2][0]:
            graph[node*2] = [graph[node][0] + 1, node]
            queue.append(node*2)
        
        if node < 100000 and graph[node][0] + 1 < graph[node+1][0]:
            graph[node+1] = [graph[node][0] + 1, node]
            queue.append(node+1)
        
        if node > 0 and graph[node][0] + 1 < graph[node-1][0]:
            graph[node-1] = [graph[node][0] + 1, node]
            queue.append(node-1)
    
    path = deque()
    node = K
    while True:
        path.appendleft(node)
        if node == N: break
        node = graph[node][1]
    
    print(graph[K][0])
    print(' '.join(map(str,path)))

# N, K = map(int, stdin.readline().split())

N, K = 5, 17

solution(N, K)