# BOJ 2744 대소문자 바꾸기
# https://www.acmicpc.net/problem/2744

from sys import stdin

def solution(word):
    return ''.join([w.lower() if w.isupper() else w.upper() for w in word])

# input
word = stdin.readline().strip()

# result
res = solution(word)
print(res)