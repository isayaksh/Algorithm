# BOJ 18114 블랙 프라이데이
# https://www.acmicpc.net/problem/18114

from sys import stdin
from bisect import bisect_left

def solution(N, C, weights):
    weights.sort()

    # 1개
    try:
        if weights[bisect_left(weights, C)] == C: return True
    except:
        pass

    # 2개
    start, end = 0, N-1
    while start < end:
        totalWeight = weights[start] + weights[end]
        if totalWeight == C: return True

        if totalWeight < C:
            # 3개
            try:
                surplusWeight = C - totalWeight
                idx = bisect_left(weights, surplusWeight)
                if idx != start and idx != end and weights[idx] == surplusWeight:
                    return True
            except:
                pass
            start += 1
        else: end -= 1
    
    return False


N, C = map(int,stdin.readline().split())
weights = list(map(int,stdin.readline().split()))

print(1) if solution(N, C, weights) else print(0)