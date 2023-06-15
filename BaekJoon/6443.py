# BOJ 6443 애너그램
# https://www.acmicpc.net/problem/6443

from sys import stdin
from collections import Counter

def soultion(word):
    N = len(word)
    used = Counter(word)

    def dfs(newWord):
        if len(newWord) == N:
            print(newWord)
            return
        for w in used:
            if used[w]:
                used[w] -= 1
                dfs(newWord+w)
                used[w] += 1
    
    dfs('')

N = int(stdin.readline())
for _ in range(N):
    word = list(sorted(list(stdin.readline().strip())))
    soultion(word)