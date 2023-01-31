# BOJ 2638 치즈
# https://www.acmicpc.net/problem/2638

from sys import stdin
from collections import deque

def solution(N, M, graph):
    answer = 0

    def bfs():

        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True

        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if (0 <= nx < M) and (0 <= ny < N) and not visited[ny][nx]:

                    # 외부 공기와 맞닿은 치즈인 경우
                    if graph[ny][nx] >= 1:
                        # 해당 치즈 가중치 + 1
                        graph[ny][nx] += 1
                    # 외부 공기와 맞닿은 외부 공기일 경우
                    else:
                        # 해당 공기 위치 추가
                        queue.append((nx, ny))
                        visited[ny][nx] = True
    
    while True:
        bfs() # 
        flag = True

        for y in range(N):
            for x in range(M):
                # 2변 이상이 외부공기와 맞닿은 경우
                if graph[y][x] >= 3:
                    # 치즈 제거
                    graph[y][x] = 0 
                    flag = False
                # 1변만 외부공기와 맞닿은 경우
                elif graph[y][x] == 2:
                    # 치즈 상태 복구
                    graph[y][x] = 1
                    flag = False
        if flag: break
        answer += 1
    return answer

# input
N, M = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

# res
res = solution(N, M, graph)
print(res)