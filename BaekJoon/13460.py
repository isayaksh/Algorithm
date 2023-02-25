# BOJ 13460 구슬 탈출 2
# https://www.acmicpc.net/problem/13460

from sys import stdin
from collections import deque

def solution(N, M, maps):

    def getPosition(x, y, d):
        dx, dy = direct[d]
        cnt = 0
        while True:
            if 0 <= x + dx < M and 0 <= y + dy < N:
                # 이동중 구멍에 빠진 상황
                if maps[y+dy][x+dx] == 'O':
                    return x + dx, y + dy, cnt + 1
                if maps[y+dy][x+dx] != '#':
                    x, y, cnt = x + dx, y + dy, cnt + 1
                    continue
            return x, y, cnt
            
    for y in range(N):
        for x in range(M):
            if maps[y][x] == 'R': rx, ry = x, y
            if maps[y][x] == 'B': bx, by = x, y
            if maps[y][x] == 'O': hx, hy = x, y

    direct = [(0,-1), (0,1), (-1,0), (1,0)] # 상하좌우

    pq = deque([(rx, ry, bx, by, 0)])
    visited = set()
    visited.add(tuple([rx, ry, bx, by]))

    while pq:
        rx, ry, bx, by, count = pq.popleft()

        # 10번 이상 이동
        if count > 10:
            break
        if (rx, ry) == (hx, hy):
            return count
        if (bx, by) == (hx, hy):
            continue
        for d in range(4):

            rnx, rny, rCnt = getPosition(rx, ry, d)
            bnx, bny, bCnt = getPosition(bx, by, d)

            if (rnx, rny) == (hx, hy) and (bnx, bny) == (hx, hy):
                continue

            if (rnx, rny) == (bnx, bny):

                dx, dy = direct[d]
                if rCnt > bCnt:
                    rnx, rny = rnx - dx, rny - dy
                else:
                    bnx, bny = bnx - dx, bny - dy
            
            vs = tuple([rnx, rny, bnx, bny])
            if vs in visited:
                continue

            if (rx, ry) == (rnx, rny) and (bx, by) == (bnx, bny):
                continue

            visited.add(vs)
            pq.append((rnx, rny, bnx, bny, count+1))
            
    return -1

N, M = map(int,stdin.readline().split())
maps = [list(stdin.readline().strip()) for _ in range(N)]

result = solution(N, M, maps)
print(result)