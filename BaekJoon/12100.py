# BOJ 12100 2048 (Easy)
# https://www.acmicpc.net/problem/12100

from sys import stdin
from collections import deque
from copy import deepcopy

answer = 0
direct = [(1,0), (0,1), (-1,0), (0,-1)]

def move(board, d):
    if d == 0: # left
        for y in range(N):
            topX = 0
            for x in range(1, N):
                if board[y][x] != 0:
                    value, board[y][x] = board[y][x], 0
                    if board[y][topX] == 0:
                        board[y][topX] = value
                    elif board[y][topX] == value:
                        board[y][topX] = value * 2
                        topX += 1
                    else:
                        topX += 1
                        board[y][topX] = value
    if d == 1: # right
        for y in range(N):
            topX = N-1
            for x in range(N-2, -1, -1):
                if board[y][x] != 0:
                    value, board[y][x] = board[y][x], 0
                    if board[y][topX] == 0:
                        board[y][topX] = value
                    elif board[y][topX] == value:
                        board[y][topX] = value * 2
                        topX -= 1
                    else:
                        topX -= 1
                        board[y][topX] = value
    if d == 2: # up
        for x in range(N):
            topY = 0
            for y in range(1, N):
                if board[y][x] != 0:
                    value, board[y][x] = board[y][x], 0
                    if board[topY][x] == 0:
                        board[topY][x] = value
                    elif board[topY][x] == value:
                        board[topY][x] = value * 2
                        topY += 1
                    else:
                        topY += 1
                        board[topY][x] = value
    if d == 3: # down
        for x in range(N):
            topY = N-1
            for y in range(N-2, -1, -1):
                if board[y][x] != 0:
                    value, board[y][x] = board[y][x], 0
                    if board[topY][x] == 0:
                        board[topY][x] = value
                    elif board[topY][x] == value:
                        board[topY][x] = value * 2
                        topY -= 1
                    else:
                        topY -= 1
                        board[topY][x] = value

def getMaxValue(board):
    result = 0
    for b in board:
        result = max(result, max(b))
    return result

N = int(stdin.readline())
board = [list(map(int,stdin.readline().split())) for _ in range(N)]

pq = deque([(board, 0)])
while pq:
    board, count = pq.popleft()

    if count == 5:
        answer = max(answer, getMaxValue(board))
        continue

    for i in range(4):
        newBoard = deepcopy(board)
        move(newBoard, i)
        pq.append((newBoard, count+1))
print(answer)