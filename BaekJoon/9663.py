# BOJ 9663 N-Queen
# https://www.acmicpc.net/problem/9663

from sys import stdin

def is_promising(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global answer
    if x == N:
        answer += 1
        return

    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            board[x] = i
            if is_promising(x):
                n_queens(x+1)

N = int(stdin.readline())

answer = 0
board = [0] * N

n_queens(0)

print(answer)