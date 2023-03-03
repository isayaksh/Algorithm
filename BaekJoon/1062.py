# BOJ 1062 가르침
# https://www.acmicpc.net/problem/1062

from sys import stdin
from itertools import combinations
from re import sub
def solution(N, K, words):

    if K < 5:
        return 0
    
    answer = 0
    words = [list(sub("a|c|i|n|t", '', word)) for word in words if word != 'antatica']
    candidateChars = set(sum(words,[]))
    charCases = combinations(candidateChars, min(len(candidateChars),K-5))

    def check(word):
        for w in word:
            if w not in availableChars:
                return False
        return True

    for case in charCases:
        availableChars = set(case)
        tmp = N - len(words)
        for word in words:
            if check(word):
                tmp += 1
        answer = max(answer, tmp)
    return answer

N, K = map(int,stdin.readline().split())
words = list(stdin.readline().strip() for _ in range(N))

res = solution(N, K, words)
print(res)