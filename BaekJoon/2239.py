# BOJ 2239 스도쿠
# https://www.acmicpc.net/problem/2239

from sys import stdin

def solution(board):
    points = [(x,y) for y in range(9) for x in range(9) if board[y][x] == 0]
    N = len(points)

    def check(x, y, num):
        for d in range(9):
            if board[y][d] == num:
                return False
            if board[d][x] == num:
                return False
        
        for dy in range((y//3)*3, (y//3)*3+3):
            for dx in range((x//3)*3, (x//3)*3+3):
                if board[dy][dx] == num:
                    return False
        return True

    def dfs(idx):
        if idx == N:
            for b in board:
                print(*b,sep="")
            exit()
        x, y = points[idx]
        for num in range(1,10):
            if check(x, y, num):
                board[y][x] = num
                dfs(idx+1)
                board[y][x] = 0
    dfs(0)

board = [list(map(int,list(stdin.readline().rstrip()))) for _ in range(9)]
solution(board)