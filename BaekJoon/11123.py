# BOJ 11123 양 한마리... 양 두마리...
# https://www.acmicpc.net/problem/11123

from sys import stdin

def solution(H, W, graph):
    answer = 0

    def bfs(x, y):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#':
                    graph[ny][nx] = '.'
                    stack.append((nx, ny))

    for y in range(H):
        for x in range(W):
            if graph[y][x] == '#':
                bfs(x, y)
                answer += 1
                
    return answer

T = int(stdin.readline())
for _ in range(T):
    H, W = map(int,stdin.readline().split())
    graph = list(list(stdin.readline().strip()) for _ in range(H))
    res = solution(H, W, graph)
    print(res)