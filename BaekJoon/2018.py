# BOJ 2018 수들의 합 5
# https://www.acmicpc.net/problem/2018
from sys import stdin

def solution(N):
    answer = 1
    sumOfNumbers = 0
    start, end = 0, 0
    while end <= N:
        if sumOfNumbers <= N:
            if sumOfNumbers == N: answer += 1
            sumOfNumbers += end
            end += 1
        else:
            sumOfNumbers -= start
            start += 1
    return answer

N = int(stdin.readline())
print(solution(N))