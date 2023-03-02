# BOJ 2580 스도쿠
# https://www.acmicpc.net/problem/2580

from sys import stdin

def solution(board):

    point = [(x,y) for y in range(9) for x in range(9) if board[y][x] == 0]
    N = len(point)

    def check(x, y, num):
        # 세로
        for dy in range(9):
            if board[dy][x] == num:
                return False
        # 가로
        for dx in range(9):
            if board[y][dx] == num:
                return False
        # 3 * 3 박스
        xr, yr = x//3*3, y//3*3
        for dy in range(yr, yr+3):
            for dx in range(xr, xr+3):
                if board[dy][dx] == num:
                    return False
        return True
    
    def dfs(idx):
        if idx == N:
            for b in board:
                print(*b)
            exit()
        x, y, = point[idx]
        for num in range(1,10):
             if check(x, y, num):
                  board[y][x] = num
                  dfs(idx+1)
                  board[y][x] = 0
    
    dfs(0)
        

board = [list(map(int,stdin.readline().split())) for _ in range(9)]
solution(board)