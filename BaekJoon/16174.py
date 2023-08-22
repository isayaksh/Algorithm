# BOJ 16174 점프왕 쩰리 (Large)
# https://www.acmicpc.net/problem/16174

from sys import stdin

def solution(N, board):
    
    visited = [[False] * N for _ in range(N)]

    def dfs(x, y, jump):        
        if board[y][x] == -1:
            return
        for dx, dy in ((1, 0), (0, 1)):
            nx, ny = x + dx * jump, y + dy * jump
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx, ny, board[ny][nx])

    dfs(0, 0, board[0][0])

    return "HaruHaru" if visited[N-1][N-1] else "Hing"

N = int(stdin.readline())
board = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, board)
print(res)