# 2565 전깃줄 < 골드 5 >
from bisect import bisect_left
from sys import stdin

def deleteCount(electricWire, N):
    electricWire = [b for a, b in electricWire] # B 위치만 추출
    # LIS 알고리즘 활용
    lis = [electricWire[0]]
    for i in range(N): 
        if electricWire[i] > lis[-1]: lis.append(electricWire[i])
        else: lis[bisect_left(lis, electricWire[i])] = electricWire[i]
    return N - len(lis)

N = int(stdin.readline())
electricWire = sorted(list(list(map(int,stdin.readline().split())) for _ in range(N))) # A 기준으로 오름차순 정렬
print(deleteCount(electricWire, N))