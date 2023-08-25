# BOJ 17413 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413

from sys import stdin

def solution(S):
    answer = ''
    sign = False
    stack = []

    for s in S:
        if s == '<':
            while stack:
                answer += stack.pop()
            answer += s
            sign = True
            continue
        if s == '>':
            answer += s
            sign = False
            continue
        if sign:
            answer += s
            continue
        if s == ' ':
            while stack:
                answer += stack.pop()
            answer += s
            continue
        stack.append(s)

    return answer.strip()


S = stdin.readline().strip() + ' '

res = solution(S)
print(res)