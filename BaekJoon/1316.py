# BOJ 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

from sys import stdin

def solution(word):
    answer = True
    used = set([word[0]])
    std = word[0]
    for i in range(1, len(word)):
        if word[i] == std: continue
        if word[i] in used:
            answer = False
            break
        else:
            std = word[i]
            used.add(word[i])
    return 1 if answer else 0

answer = 0

N = int(stdin.readline())
for _ in range(N):
    word = stdin.readline().strip()
    answer += solution(word)

print(answer)