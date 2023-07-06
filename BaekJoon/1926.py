# BOJ 1926 그림
# https://www.acmicpc.net/problem/1926

from sys import stdin
from collections import deque

def solution(height, width, draw):

    count, maxSize = 0, 0
    visited = [[False] * width for _ in range(height)]

    def dfs(x, y):
        size = 1
        queue = deque([(x, y)])
        visited[y][x] = True
        while queue:
            x, y, = queue.popleft()
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and draw[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    size += 1
                    queue.append((nx, ny))
        return size

    for y in range(height):
        for x in range(width):
            if draw[y][x] == 1 and not visited[y][x]:
                count += 1
                maxSize = max(maxSize, dfs(x, y))
    
    return count, maxSize

height, width = map(int,stdin.readline().split())
draw = list(list(map(int,stdin.readline().split())) for _ in range(height))

count, maxSize = solution(height, width, draw)
print(count)
print(maxSize)