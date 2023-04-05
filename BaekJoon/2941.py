# BOJ 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

from sys import stdin
from re import findall

def solution(word):
    return len(findall('c=|c-|dz=|d-|lj|nj|s=|z=|.',word))

# input
word = stdin.readline().strip()

# result
print(solution(word))