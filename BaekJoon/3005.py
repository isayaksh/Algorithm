# BOJ 3005 크로스워드 퍼즐 쳐다보기
# https://www.acmicpc.net/problem/3005

from sys import stdin

def solution(R, C, puzzle):
    
    candidates = []
    # 가로
    for line in puzzle:
        for candidate in ''.join(line).split('#'):
            if len(candidate) >= 2:
                candidates.append(candidate)
    # 세로
    for x in range(C):
        for candidate in ''.join([puzzle[y][x] for y in range(R)]).split('#'):
            if len(candidate) >= 2:
                candidates.append(candidate)
    
    candidates.sort()
    return candidates[0]

R, C = map(int,stdin.readline().split())
puzzle = list(list(stdin.readline().strip()) for _ in range(R))

res = solution(R, C, puzzle)
print(res)