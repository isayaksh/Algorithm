# BOJ 3980 선발 명단
# https://www.acmicpc.net/problem/3980

from sys import stdin

def solution(ability):

    used = [False] * 11

    def dfs(idx, total_ability):
        global answer
        if idx == 11:
            answer = max(answer, total_ability)
            return
        for i in range(11):
            if ability[idx][i] != 0 and not used[i]:
                used[i] = True
                dfs(idx+1, total_ability + ability[idx][i])
                used[i] = False

    dfs(0, 0)

for _ in range(int(stdin.readline())):
    answer = 0
    ability = list(list(map(int,stdin.readline().split())) for _ in range(11))
    solution(ability)
    print(answer)