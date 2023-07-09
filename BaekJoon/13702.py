# BOJ 13702 이상한 술집
# https://www.acmicpc.net/problem/13702

from sys import stdin

def solution(N, K, drinks):
    start, end = 1, max(drinks)
    while start <= end:
        mid = (start + end) // 2
        quotient = sum([drink//mid for drink in drinks])
        if quotient < K: end = mid - 1
        else: start = mid + 1
    
    return end

N, K = map(int,stdin.readline().split())
drinks = list(int(stdin.readline()) for _ in range(N))

res = solution(N, K, drinks)
print(res)