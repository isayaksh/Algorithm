# BOJ 10703 유성
# https://www.acmicpc.net/problem/10703

from sys import stdin
from collections import defaultdict

def solution(R, S, picture):

    def clearMeteor():
        for x, y in meteor:
            picture[y][x] = '.'
    
    def drawMeteor(gap):
        for x, y in meteor:
            picture[y+gap][x] = 'X'
    
    def recoveringPictureAfterMeteorShower(gap):
        clearMeteor()
        drawMeteor(gap)

    # 유성의 초기 위치
    meteor = [(x, y) for y in range(R) for x in range(S) if picture[y][x] == 'X']
    
    # 유성의 하단 부분
    bottomOfMeteor = defaultdict(int)
    for x, y in meteor:
        if bottomOfMeteor[x] < y:
            bottomOfMeteor[x] = y
    
    # 유성 낙하
    gap = 1
    while True:
        for x, y in bottomOfMeteor.items():
            if picture[y+gap][x] == '#':
                recoveringPictureAfterMeteorShower(gap-1)
                return picture
        gap += 1

# input
R, S = map(int,stdin.readline().split())
picture = list(list(stdin.readline().strip()) for _ in range(R))

# result
result = solution(R, S, picture)
for res in result:
    print(''.join(res))