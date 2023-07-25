# BOJ 16139 인간-컴퓨터 상호작용
# https://www.acmicpc.net/problem/16139

from sys import stdin

def solution(S, q, questions):
    N = len(S)
    counter = [[0] * (N + 1) for _ in range(26)]
    
    for y in range(26):
        alpha = chr(y+97)
        for x in range(N):
            counter[y][x+1] = counter[y][x] + 1 if alpha == S[x] else counter[y][x]

    for a, l, r in questions:
        y = ord(a) - 97
        print(counter[y][int(r)+1] - counter[y][int(l)])

S = stdin.readline().strip()
q = int(stdin.readline())
questions = list(list(stdin.readline().split()) for _ in range(q))

solution(S, q, questions)