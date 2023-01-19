# 10026 적록색약 < 골드 5>
from sys import stdin
from collections import deque

def solution1(N, graph):
    answer1, answer2 = 0, 0
    visited1 = [[False] * N for _ in range(N)]
    visited2 = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            
            target = graph[y][x]

            # 적록색약이 아닌 사람
            if not visited1[y][x]:
                visited1[y][x] = True
                answer1 += 1
                queue = deque([(x, y)])

                while queue:
                    cx, cy  = queue.popleft()
                    for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
                        nx, ny = cx + dx, cy + dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or target != graph[ny][nx] or visited1[ny][nx]: continue
                        visited1[ny][nx] = True
                        queue.append((nx, ny))
            
            # 적록색약인 사람
            if not visited2[y][x]:
                visited2[y][x] = True
                answer2 += 1
                queue = deque([(x, y)])

                while queue:
                    cx, cy  = queue.popleft()
                    for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
                        nx, ny = cx + dx, cy + dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited2[ny][nx]: continue
                        if target == 'B' and graph[ny][nx] != 'B': continue
                        if target != 'B' and graph[ny][nx] == 'B': continue
                        visited2[ny][nx] = True
                        queue.append((nx, ny))
                
    return answer1, answer2

N = int(stdin.readline())
graph = [list(stdin.readline().strip()) for _ in range(N)]

r1, r2 = solution1(N, graph)
print(r1, r2)