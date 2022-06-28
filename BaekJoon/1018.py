# 1018 체스판 다시 칠하기 < 실버 4 >
from sys import stdin
def paint_count(X,Y):
    cnt1, cnt2 = 0, 0
    for y in range(Y, Y + 8):
        for x in range(X, X + 8):
            if (x+y)%2:
                if board[y][x] != 'B': cnt1 += 1
                if board[y][x] != 'W': cnt2 += 1
            else:
                if board[y][x] != 'W': cnt1 += 1
                if board[y][x] != 'B': cnt2 += 1
    return min(cnt1, cnt2)
board = []
result = 65
N, M = map(int,stdin.readline().split()) # 세로, 가로
for _ in range(N):
    board.append(list(stdin.readline().rstrip()))
for y in range(N-7):
    for x in range(M-7):
        result = min(result, paint_count(x,y))
print(result)
