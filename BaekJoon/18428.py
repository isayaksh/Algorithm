# BOJ 18428 감시 피하기
# https://www.acmicpc.net/problem/18428

from sys import stdin

def solution(N, graph):
    
    teacher = [(x, y) for y in range(N) for x in range(N) if graph[y][x] == 'T']

    def check():
        for x, y in teacher:
            stack = [(x, y, dx, dy) for dx, dy in ((1,0), (0,1), (-1,0), (0,-1))]
            while stack:
                x, y, dx, dy = stack.pop()
                if graph[y][x] == 'S': return False
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] != 'O':
                    stack.append((nx, ny, dx, dy))
        return True

    for i in range(N*N-2):
        x1, y1 = i%N, i//N
        if graph[y1][x1] != 'X': continue
        for j in range(i+1, N*N-1):
            x2, y2 = j%N, j//N
            if graph[y2][x2] != 'X': continue
            for k in range(j+1, N*N):
                x3, y3 = k%N, k//N
                if graph[y3][x3] != 'X': continue
                # 3개의 장애물을 설치
                graph[y1][x1], graph[y2][x2], graph[y3][x3] = 'O', 'O', 'O'
                if check():
                    return 'YES'
                graph[y1][x1], graph[y2][x2], graph[y3][x3] = 'X', 'X', 'X'
    
    return 'NO'

N = int(stdin.readline())
graph = list(list(stdin.readline().split()) for _ in range(N))

result = solution(N, graph)
print(result)