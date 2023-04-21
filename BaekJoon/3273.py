# BOJ 3273 두 수의 합
# https://www.acmicpc.net/problem/3273

from sys import stdin

def solution(n, numbers, x):
    answer = 0
    numbers.sort()
    start, end = 0, n-1
    while start < end:
        total = numbers[start] + numbers[end]
        if total <= x:
            if total == x: answer += 1
            start += 1
        else:
            end -= 1
    return answer

# input
n = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))
x = int(stdin.readline())

# result
result = solution(n, numbers, x)
print(result)