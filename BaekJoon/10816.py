# BOJ 10816 숫자 카드 2
# https://www.acmicpc.net/problem/10816

from sys import stdin
from collections import Counter

def solution(N, numbers, M, findNumbers):
    haveNumbers = Counter(numbers)
    return [haveNumbers[number] for number in findNumbers]

N = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
findNumbers = list(map(int,stdin.readline().split()))

res = solution(N, numbers, M, findNumbers)
print(' '.join(map(str,res)))