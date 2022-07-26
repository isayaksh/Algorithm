# 14891 톱니바퀴 < 골드 5 >
from collections import deque
from sys import stdin

def rotate(gear,rotation):
    if rotation == 1: gear.appendleft(gear.pop()) # 시계방향
    else: gear.append(gear.popleft()) # 반시계방향
    return gear

gear = [deque(list(stdin.readline().strip())) for _ in range(4)]

K = int(stdin.readline())
for _ in range(K):
    num, rotation = map(int,stdin.readline().split())
    num -= 1
    # 톱니바퀴 회전
    gear[num] = rotate(gear[num],rotation)

    # 회전한 톱니바퀴 기준 왼쪽
    rot = rotation
    for i in range(num,0,-1):
        if gear[i][6+rot] == gear[i-1][2]: break
        rot *= -1
        gear[i-1] = rotate(gear[i-1],rot)
    
    # 회전한 톱니바퀴 기준 오른쪽
    rot = rotation
    for i in range(num,3):
        if gear[i][2+rot] == gear[i+1][6]: break
        rot *= -1
        gear[i+1] = rotate(gear[i+1],rot)

result = 0
for i in range(4):
    if gear[i][0] == '1':
        result += 2**i;
print(result)