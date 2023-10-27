# BOJ 1668 트로피 진열
# https://www.acmicpc.net/problem/1668

from sys import stdin

def solution(N, trophyList):
    
    def getCount(trophyList):
        count, height = 0, 0
        for trophy in trophyList:
            if trophy  > height:
                count, height = count + 1, trophy
        return count

    return getCount(trophyList), getCount(trophyList[::-1])

N = int(stdin.readline())
trophyList = list(int(stdin.readline()) for _ in range(N))

left, right = solution(N, trophyList)
print(left)
print(right)