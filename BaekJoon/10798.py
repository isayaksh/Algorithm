# BOJ 10798 세로읽기
# https://www.acmicpc.net/problem/10798

from sys import stdin

def solution(words):
    answer = ''
    length = [len(word) for word in words] # 각 단어의 길이
    N = max(length) # 가장 긴 단어의 길이

    for x in range(N):
        for y in range(5):
            answer += words[y][x] if x < length[y] else ''

    return answer

# input
words = list(stdin.readline().strip() for _ in range(5))

# result
res = solution(words)
print(res)