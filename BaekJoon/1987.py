# BOJ 1987 알파벳
# https://www.acmicpc.net/problem/1987

from sys import stdin

def solution(R, C, graph):
    answer = 0
    queue = set([(0, 0, graph[0][0])])
    while queue:
        x, y, path = queue.pop()
        answer = max(answer, len(path))
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] not in path:
                queue.add((nx, ny, path+graph[ny][nx]))
    return answer

# input
R, C = map(int,stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(R)]

# result
result = solution(R, C, graph)
print(result)