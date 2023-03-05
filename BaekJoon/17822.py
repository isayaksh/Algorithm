# BOJ 17822 원판 돌리기
# https://www.acmicpc.net/problem/17822

from sys import stdin
from collections import deque

def solution(N, M, T, disc, turnCase):

    # 1. 회전
    def turn(x, d, k):
        d = 1 if d == 0 else -1
        for dx in range(x, N+1, x):
            disc[dx-1].rotate(d*k)

    # 2. 인접한 같은 수
    def checkAdjacency():
        changePoint = []
        for y in range(N):
            for x in range(M):
                if disc[y][x] != 0:
                    if disc[y][x] == disc[y][x-1]:
                        changePoint.append((x,y,x-1,y))
                    if y != 0 and disc[y][x] == disc[y-1][x]:
                        changePoint.append((x,y,x,y-1))

        # 2-1. 인접한 같은 수 제거
        for x1, y1, x2, y2 in changePoint:
            disc[y1][x1], disc[y2][x2] = 0, 0
        
        # 2-2. 인접한 같은 수 X, 평균 
        if not changePoint:
            total, count = 0, 0
            for y in range(N):
                for x in range(M):
                    if disc[y][x] != 0:
                        count += 1
                        total += disc[y][x]
            # Exception : ZeroDivisionError
            if count == 0:
                return
            avg = total/count
            for y in range(N):
                for x in range(M):
                    if disc[y][x] != 0:
                        if disc[y][x] > avg:
                            disc[y][x] -= 1
                        elif disc[y][x] < avg:
                            disc[y][x] += 1    
    
    for x, d, k in turnCase:
        turn(x, d, k)
        checkAdjacency()

    return sum(map(sum,disc))

N, M, T = map(int,stdin.readline().split())
disc = list(deque(map(int,stdin.readline().split())) for _ in range(N))
spin = list(list(map(int,stdin.readline().split())) for _ in range(T))

res = solution(N, M, T, disc, spin)
print(res)