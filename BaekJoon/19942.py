# BOJ 19942 다이어트
# https://www.acmicpc.net/problem/19942

from sys import stdin, maxsize
from heapq import heappop, heappush

def solution(N, mp, mf, ms, mv, ingredients):
    minPrice = maxsize
    minCase = []

    heap = []
    for i in range(N):
        heappush(heap, [ingredients[i][4], [i+1]] + [j for j in ingredients[i][:4]])
    
    while heap:
        price, case, p, f, s, v = heappop(heap)
        if price > minPrice: continue
        if p>=mp and f>=mf and s>=ms and v>=mv:
            if price == minPrice:
                minCase.append(case)
            else:
                minPrice = price
                minCase = [case]
        else:
            for i in range(case[-1], N):
                np, nf, ns, nv, nprice = ingredients[i]
                heappush(heap, [price + nprice, case+[i+1], p+np, f+nf, s+ns, v+nv])
    minCase.sort()
    if minPrice == maxsize:
        print(-1)
    else:
        print(minPrice)
        print(*minCase[0])

# input
N = int(stdin.readline())
mp, mf, ms, mv = map(int,stdin.readline().split())
ingredients = list(list(map(int,stdin.readline().split())) for _ in range(N))

# result
solution(N, mp, mf, ms, mv, ingredients)
