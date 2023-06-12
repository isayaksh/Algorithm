# BOJ 17140 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140

from sys import stdin
from collections import defaultdict
from itertools import chain

def solution(r, c, k, A):
    
    def operationR(column, row):
        result = []
        maxLength = 0
        for y in range(row):
            weight = defaultdict(int)
            for x in range(column):
                if A[y][x]!=0: weight[A[y][x]] += 1
            result.append(list(chain(*sorted(weight.items(), key=lambda x : (x[1], x[0]))))[:100])
            maxLength = max(maxLength, len(weight)*2)
        for y in range(row):
            for _ in range(maxLength-len(result[y])):
                result[y].append(0)
        return result
            
    def operationC(column, row):
        result = []
        maxLength = 0
        for x in range(column):
            weight = defaultdict(int)
            for y in range(row):
                if A[y][x]!=0: weight[A[y][x]] += 1
            result.append(list(chain(*sorted(weight.items(), key=lambda x : (x[1], x[0]))))[:100])
            maxLength = max(maxLength, len(weight)*2)
        for x in range(column):
            for _ in range(maxLength-len(result[x])):
                result[x].append(0)
        return list(map(list, zip(*result)))

    for i in range(101):
        try:
            if A[r-1][c-1] == k: return i
        except:
            pass
        column, row = len(A[0]), len(A)
        A = operationR(column, row) if column <= row else operationC(column, row)
    return -1

r, c, k = map(int,stdin.readline().split())
A = list(list(map(int,stdin.readline().split())) for _ in range(3))

res = solution(r, c, k, A)
print(res)