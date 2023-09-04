# BOJ 9613 GCD 합
# https://www.acmicpc.net/problem/9613

from sys import stdin
from math import gcd

def solution(numbers):
    answer = 0
    N = len(numbers)
    for i in range(1, N-1):
        for j in range(i+1, N):
            answer += gcd(numbers[i], numbers[j])
    return answer

T = int(stdin.readline())
for _ in range(T):
    numbers = list(map(int,stdin.readline().split()))
    res = solution(numbers)
    print(res)