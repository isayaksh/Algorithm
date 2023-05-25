# BOJ 2467 용액
# https://www.acmicpc.net/problem/2467

from sys import stdin, maxsize

def solution(N, numbers):
    a1, a2 = 0, 0
    std = maxsize

    start, end = 0, N-1
    while start < end:
        total = numbers[end] + numbers[start]
        if abs(total) <= std:
            std = abs(total)
            a1, a2 = numbers[start], numbers[end]
        if total < 0:
            start += 1
        else:
            end -= 1
    return a1, a2


N = int(stdin.readline())
numbers = list(sorted(map(int,stdin.readline().split())))

a1, a2 = solution(N, numbers)
print(a1, a2)