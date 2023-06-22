# BOJ 2671 잠수함식별
# https://www.acmicpc.net/problem/2671

from sys import stdin
from re import compile, fullmatch

def solution(sound):
    pattern = compile("(100+1+|01)+")
    print(pattern)
    return "SUBMARINE" if pattern.fullmatch(sound) else "NOISE"

sound = stdin.readline().strip()
res = solution(sound)
print(res)



# def test():
#     testCases = ['1001', '01', '100001', '010101', '1000001110101', '1001110101', '0101010101', '10010110000001111101', '01010101011000111', '10000111001111']

#     for testCase in testCases:
#         res = solution(testCase)
#         print(res)
# test()