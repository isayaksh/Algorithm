# BOJ 1475 방 번호
# https://www.acmicpc.net/problem/1475

from sys import stdin
from collections import Counter

def solution(N):
    counter = Counter(N)
    candidate1 = (counter['6'] + counter['9'])//2 + (counter['6'] + counter['9'])%2
    candidate2 = max([v for k, v in counter.items() if (k != '9' and k != '6')] + [0])
    return max(candidate1, candidate2)

# input
N = stdin.readline().strip()

# result
result = solution(N)
print(result)