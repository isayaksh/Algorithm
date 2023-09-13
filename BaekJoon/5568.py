# BOJ 5568 카드 놓기
# https://www.acmicpc.net/problem/5568

from sys import stdin
from itertools import permutations

def solution(n, k, numbers):
    answer = set()
    for number in permutations(numbers, k):
        answer.add(''.join(number))
    return len(answer)

n = int(stdin.readline())
k = int(stdin.readline())
numbers = list(stdin.readline().strip() for _ in range(n))

res = solution(n, k, numbers)
print(res)