# BOJ 16236 아기 상어
# https://www.acmicpc.net/problem/16236

from sys import stdin
from collections import deque

def solution(N, graph):

    def bfs(x, y, size):
        graph[y][x] = 0
        visited = [[False] * N for _ in range(N)]
        visited[y][x] = True

        cases = []

        queue = deque([(x, y, 0)])
        while queue:
            x, y, t = queue.popleft()
            for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] <= size:
                    if graph[ny][nx] != 0 and graph[ny][nx] < size:
                        cases.append((t+1, nx, ny))
                    queue.append((nx, ny, t+1))
                    visited[ny][nx] = True

        return (-1, -1, -1) if not cases else sorted(cases, key=lambda x : (x[0], x[2], x[1]))[0]
    
    answer = 0
    size, eat = 2, 2

    # 아기 상어의 위치(bsx, bsy)
    bs = [(x, y) for x in range(N) for y in range(N) if graph[y][x] == 9]
    bsx, bsy = bs[0]
    
    while True:
        # 거리가 가장 가까운 먹을 수 있는 물고기 찾기
        time, bsx, bsy = bfs(bsx, bsy, size)

        # 더 이상 먹을 수 있는 물고기가 공간에 없다면
        if bsx == -1 and bsy == -1 and time == -1:
            break

        # 이동시간 갱신
        answer += time

        # 크기 갱신
        eat -= 1
        if eat == 0:
            size += 1
            eat = size
    return answer

# input
N = int(stdin.readline())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

# result
result = solution(N, graph)
print(result)