# 15686 치킨 배달 <골드 5>
from sys import stdin
from itertools import combinations

def minimumChickenDistance(N,M,MAP):
    answer = 101
    chickenHouse = [[x,y] for x in range(N) for y in range(N) if MAP[y][x] == 2]
    house = [[x,y] for x in range(N) for y in range(N) if MAP[y][x] == 1]
    for chick in combinations(chickenHouse, M):
        distance = 0
        for hx, hy in house:
            tmp = 101
            for cx, cy in chick:
                tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
            distance += tmp
        answer = min(answer, distance)
    return answer

N, M = map(int,stdin.readline().split())
MAP = list(list(map(int,stdin.readline().split())) for _ in range(N))

print(minimumChickenDistance(N,M,MAP))