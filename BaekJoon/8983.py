# BOJ 8983 사냥꾼
# https://www.acmicpc.net/problem/8983

from sys import stdin
from bisect import bisect_left, bisect_right

def solution(N, M, L, X, animal):
    answer = 0
    X.sort()

    for x, y in animal:
        idx = bisect_left(X, x)
        
        for i in range(-1, 2):
            if 0 <= idx + i < M:
                if L - abs(x - X[idx+i]) >= y:
                    answer +=1
                    break

    return answer

M, N, L = map(int,stdin.readline().split())
X = list(map(int,stdin.readline().split()))
animal = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, M, L, X, animal)
print(res)