# BOJ 15918 랭퍼든 수열쟁이야!!
# https://www.acmicpc.net/problem/15918

from sys import stdin

def solution(n, x, y):
    number = [0 for _ in range(n*2)]

    staticNumber = y-x-1
    number[x-1], number[y-1] = staticNumber, staticNumber

    def dfs(num):
        global answer
        if staticNumber == num:
            dfs(num-1)
        if num == 0:
            answer += 1
            return
        for i in range(n*2):
            if number[i] == 0 and i+num+1 < n*2 and number[i+num+1] == 0:
                number[i], number[i+num+1] = num, num
                dfs(num-1)
                number[i], number[i+num+1] = 0, 0
    dfs(n)

answer = 0
n, x, y = map(int,stdin.readline().split())

solution(n, x, y)
print(answer)