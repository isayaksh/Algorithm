# BOJ 12871 무한 문자열
# https://www.acmicpc.net/problem/12871

from sys import stdin
from math import gcd

def solution(s, t):

    # 최소 공배수
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    sLen, tLen = len(s), len(t)

    s = s * (lcm(sLen, tLen) // sLen)
    t = t * (lcm(sLen, tLen) // tLen)

    return 1 if s == t else 0

s = stdin.readline().strip()
t = stdin.readline().strip()

res = solution(s, t)
print(res)