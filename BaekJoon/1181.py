# BOJ 1181 단어 정렬
# https://www.acmicpc.net/problem/1181

from sys import stdin

def solution(N, words):
    words = list(set(words))
    words.sort(key=lambda x:(len(x), x))
    return words

N = int(stdin.readline())
words = list(stdin.readline().strip() for _ in range(N))

result = solution(N, words)
for res in result:
    print(res)