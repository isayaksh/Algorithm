# BOJ 21939 문제 추천 시스템 Version 1
# https://www.acmicpc.net/problem/21939

from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict

def solution(N, M, problems, orders):

    minHeap, maxHeap = [], []
    solved = defaultdict(int)

    for P, L in problems:
        heappush(minHeap, (L, P))
        heappush(maxHeap, (-L, -P))
    
    for order in orders:
        # recommend x
        if order[0] == 'recommend':
            if order[1] == '1':
                while solved[abs(maxHeap[0][1])] != 0:
                    solved[abs(maxHeap[0][1])] -= 1
                    heappop(maxHeap) 
                print(-maxHeap[0][1])
            if order[1] == '-1':
                while solved[minHeap[0][1]] != 0:
                    solved[minHeap[0][1]] -= 1
                    heappop(minHeap)
                print(minHeap[0][1])
        # add P L
        if order[0] == 'add':
            P, L = int(order[1]), int(order[2])
            heappush(minHeap, (L, P))
            heappush(maxHeap, (-L, -P))
            
        # solved P
        if order[0] == 'solved':
            solved[int(order[1])] += 1

N = int(stdin.readline())
problems = list(list(map(int,stdin.readline().split())) for _ in range(N))
M = int(stdin.readline())
orders = list(list(stdin.readline().split()) for _ in range(M))

solution(N, M, problems, orders)