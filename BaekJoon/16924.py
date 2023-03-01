# BOJ 16924 십자가 찾기
# https://www.acmicpc.net/problem/16924

from sys import stdin

def solution(N, M, board):

    def checkCross(x, y, size):
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx * size, y + dy * size
            if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] == '.':
                return False
        return True

    def findAllCases():
        cases = []
        for y in range(1, N):
            for x in range(1,M):
                if board[y][x] == '*':
                    size = 1
                    while checkCross(x, y, size):
                        size += 1
                    if size != 1:
                        cases.append((x, y, size-1))
        return cases
    
    def eraseCross(x, y, size):
        for s in range(size+1):
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx * s, y + dy * s
                board[ny][nx] = '.'

    
    def checkAllClear():
        for y in range(N):
            for x in range(M):
                if board[y][x] != '.':
                    return False
        return True
    
    answer = []
    cases = findAllCases()
    cases.sort(key=lambda x:x[2], reverse=True)
    for x, y, size in cases:
        answer.append((y+1, x+1, size))
        eraseCross(x, y, size)
        if checkAllClear():
            return answer
    return -1

N, M = map(int,stdin.readline().split())
board = [list(stdin.readline().strip()) for _ in range(N)]

result = solution(N, M, board)
if result != -1:
    print(len(result))
    for res in result:
        print(*res)
else:
    print(-1)