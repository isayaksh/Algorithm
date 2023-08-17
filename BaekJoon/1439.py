# BOJ 1439 뒤집기
# https://www.acmicpc.net/problem/1439

from sys import stdin

def solution(S):
    answer = 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            answer += 1
    return answer // 2

S = stdin.readline().strip()

res = solution(S)
print(res)