# BOJ 19699 소-난다!
# https://www.acmicpc.net/problem/19699

from sys import stdin
from itertools import combinations
from math import sqrt

def solution(N, M, weights):

    def isPrime(num):
        for i in range(2, int(sqrt(num))+1):
            if not num%i:
                return False
        return True
    
    answer = set()

    for totalWeight in combinations(weights, M):
        sumTotalWeight = sum(totalWeight)
        if isPrime(sumTotalWeight):
            answer.add(sumTotalWeight)
    
    return list(sorted(answer))

N, M = map(int,stdin.readline().split())
weights = list(map(int,stdin.readline().split()))

res = solution(N, M, weights)
print(' '.join(map(str, res))) if res else print(-1)