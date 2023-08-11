# BOJ 2578 빙고
# https://www.acmicpc.net/problem/2578

from sys import stdin

def solution(board, sequence):
    def check(x, y):
        count = 0
        if all([visited[y][i] for i in range(5)]):
            count += 1
        if all([visited[i][x] for i in range(5)]):
            count += 1
        if x == y and all([visited[i][i] for i in range(5)]):
            count += 1
        if x + y == 4 and all([visited[i][4-i] for i in range(5)]):
            count += 1
        return count

    answer = 0
    visited = [[False] * 5 for _ in range(5)]    

    locationDict = dict()
    for y in range(5):
        for x in range(5):
            locationDict[board[y][x]] = (x, y)
    
    for i in range(25):
        x, y = locationDict[sequence[i]]
        visited[y][x] = True
        answer += check(x, y)
        if answer >= 3:
            print(i+1)
            return

board = list(list(map(int,stdin.readline().split())) for _ in range(5))
sequence = []
for _ in range(5):
    sequence.extend(list(map(int,stdin.readline().split())))

solution(board, sequence)