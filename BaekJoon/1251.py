# BOJ 1251 단어 나누기
# https://www.acmicpc.net/problem/1251

from sys import stdin
from itertools import combinations

def solution(word):
    answer = 'z'*50
    for sep1, sep2 in combinations(range(1, len(word)), 2):
        answer = min(answer, word[:sep1][::-1] + word[sep1:sep2][::-1] + word[sep2:][::-1])
    return answer

# input
word = stdin.readline().strip()

# result
result = solution(word)
print(result)