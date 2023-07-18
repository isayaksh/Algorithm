# BOJ 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

from sys import stdin

def solution(N, numbers):
    return sum(map(int,list(numbers)))

N = int(stdin.readline())
numbers = stdin.readline().strip()

res = solution(N, numbers)
print(res)