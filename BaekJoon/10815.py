# BOJ 10815 숫자 카드
# https://www.acmicpc.net/problem/10815

from sys import stdin

def solution(N, haveNumbers, M, checkNumbers):
    return [1 if number in haveNumbers else 0 for number in checkNumbers]

N = int(stdin.readline())
haveNumbers = set(map(int,stdin.readline().split()))
M = int(stdin.readline())
checkNumbers = list(map(int,stdin.readline().split()))

res = solution(N, haveNumbers, M, checkNumbers)
print(*res)