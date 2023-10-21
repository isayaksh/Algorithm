# BOJ 20114 미아 노트
# https://www.acmicpc.net/problem/20114

from sys import stdin

def solution(N, H, W, pattern):

    def extractWord(point):
        for y in range(H):
            for x in range(point*W, point*W+W):
                if pattern[y][x] != '?':
                    return pattern[y][x]
        return '?'
    
    answer = ['?'] * N

    for i in range(N):
        answer[i] = extractWord(i)

    return ''.join(answer)

N, H, W = map(int,stdin.readline().split())
pattern = list(list(stdin.readline().strip()) for _ in range(H))

res = solution(N, H, W, pattern)
print(res)