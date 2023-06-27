# BOJ 19532 수학은 비대면강의입니다
# https://www.acmicpc.net/problem/19532
from sys import stdin

def solution(a, b, c, d, e, f):
    return int((c*e-b*f)/(a*e-b*d)), int((a*f-c*d)/(a*e-b*d))

a, b, c, d, e, f = map(int,stdin.readline().split())

x, y = solution(a, b, c, d, e, f)
print(x, y)