# BOJ 18116 로봇 조립
# https://www.acmicpc.net/problem/18116

from sys import stdin

def solution(N, orders):

    parent = [i for i in range(1000001)]
    value = [1] * 1000001
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x, y = find(x), find(y)
        if x == y: return
        parent[max(x, y)] = min(x, y)
        value[min(x,y)] += value[max(x,y)]

    for order in orders:
        if order[0] == 'I':
            union(int(order[1]), int(order[2]))
        elif order[0] == 'Q':
            print(value[find(int(order[1]))])

N = int(stdin.readline())
orders = list(list(stdin.readline().strip().split()) for _ in range(N))

solution(N, orders)