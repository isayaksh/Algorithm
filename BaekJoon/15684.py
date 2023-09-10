# BOJ 15684 사다리 조작
# https://www.acmicpc.net/problem/15684

from sys import stdin, maxsize

answer = maxsize

def solution(N, M, H, lines):

    # 사다리 타기 게임
    def ladderGame():
        for x in range(1, N+1):
            dx = x
            for y in range(1, H+1):
                if graph[y][dx] != 0:
                    dx = graph[y][dx]
            if dx != x:
                return False
        return True
    
    def dfs(x, y, cnt):
        global answer

        # 일치
        if ladderGame():
            answer = min(answer, cnt)
            return
        
        if cnt == 3:
            return

        for dx in range(x, N):
            if not graph[y][dx] and not graph[y][dx+1]:
                graph[y][dx], graph[y][dx+1] = dx+1, dx
                dfs(dx+2, y, cnt+1)
                graph[y][dx], graph[y][dx+1] = 0, 0
        
        for dy in range(y+1, H+1):
            for dx in range(1, N):
                if not graph[dy][dx] and not graph[dy][dx+1]:
                    graph[dy][dx], graph[dy][dx+1] = dx+1, dx
                    dfs(dx+2, dy, cnt+1)
                    graph[dy][dx], graph[dy][dx+1] = 0, 0

    # graph 초기화
    graph = [[0] * (N+1) for _ in range(H+1)]
    for a, b in lines:
        graph[a][b] = b+1
        graph[a][b+1] = b
    
    dfs(1, 1, 0)
    print(answer if answer != maxsize else -1)

N, M, H = map(int,stdin.readline().split())
lines = list(list(map(int,stdin.readline().split())) for _ in range(M))

# N, M, H = 5, 5, 6
# lines = [[1, 1], [3, 2], [2, 3], [5, 1], [5, 4]]

solution(N, M, H, lines)