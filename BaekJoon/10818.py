# BOJ 10818 최소, 최대
# https://www.acmicpc.net/problem/10818

from sys import stdin

def solution(N, numbers):
    return min(numbers), max(numbers)

N = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))

minValue, maxValue = solution(N, numbers)
print(minValue, maxValue)