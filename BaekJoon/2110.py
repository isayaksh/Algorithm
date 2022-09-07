# 2110 공유기 설치 < 골드 5 >
from sys import stdin

def setRouter(N,C,X):
    start, end = 1, X[-1] - X[0]
    answer = 0
    while start <= end:
        #print("start : {}, end : {}".format(start, end))
        mid = (start+end)//2
        cnt = 1
        curLoc = X[0]
        for i in range(1,N):
            if X[i] >= curLoc + mid:
                cnt += 1
                curLoc = X[i]
        if cnt < C: end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer

N, C = map(int,stdin.readline().split())
X = sorted([int(stdin.readline()) for _ in range(N)])

print(setRouter(N,C,X))