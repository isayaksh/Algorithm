# BOJ 7490 0 만들기
# https://www.acmicpc.net/problem/7490

from sys import stdin

def solution(N):
    def dfs(opr, i):
        opr += str(i)
        if i == N:
            reCase = opr.replace(' ', '')
            if 0 == eval(reCase):
                print(opr)
            return
        dfs(opr+' ', i+1)
        dfs(opr+'+', i+1)
        dfs(opr+'-', i+1)
    dfs('', 1)

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    solution(N)
    print()