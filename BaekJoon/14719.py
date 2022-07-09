# 14719 빗물 < 골드 5 >
from sys import stdin

def SumOfRainWater(W,blocks):
    result = 0
    for i in range(1,W-1):
        leftWall, rightWall = max(blocks[:i]), max(blocks[i+1:])
        std = min(leftWall,rightWall)
        if std > blocks[i]: result += std - blocks[i]
    return result

H, W = map(int,stdin.readline().split())
blocks = tuple(map(int,stdin.readline().split()))
print(SumOfRainWater(W,blocks))