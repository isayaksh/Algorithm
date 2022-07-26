# 14503 로봇 청소기 < 골드 5 >
from sys import stdin
move = [(0,-1),(1,0),(0,1),(-1,0)] # 북, 동, 남, 서
# 현재 위치와 바라보는 방향을 기준으로 왼쪽의 영역이 청소가 되었는지 확인
def checkLeft(x, y, d):
    nx = x + move[d][0]
    ny = y + move[d][1]
    if area[ny][nx] == 0: return True
    else: return False
# 현재 위치를 기준으로 사방(동서남북)의 영역이 청소가 되었는지 확인
def checkFourDirection(x,y):
    result = True
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if area[ny][nx] == 0: result = False
    return result
# 현재 위치와 방향을 기준으로 뒤 영역이 벽인지 확인
def checkBack(x,y,d):
    d = (d+2)%4
    nx = x + move[d][0]
    ny = y + move[d][1]
    if area[ny][nx] == 1: return True
    else: return False
# 현재 위치와 방향을 기준으로 뒤로 이동
def moveBack(x,y,d):
    d = (d+2)%4
    nx = x + move[d][0]
    ny = y + move[d][1]
    return nx, ny

def func(x, y, d):
    cnt = 0
    while True:
        if area[y][x] == 0:
            area[y][x] = 2 # 1. 현재 위치를 청소한다.
            cnt += 1 # 청소 횟수 + 1
        d = (d+3)%4
        if checkLeft(x,y,d): # 2-1.왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
            # 한 칸을 전진하고
            x += move[d][0]
            y += move[d][1]
            continue # 1번부터 진행한다.
        if checkFourDirection(x,y): # 2-3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는,
            d = (d+1)%4 # 바라보는 방향을 유지한 채로
            if checkBack(x,y,d): break # 2-4. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
            x, y = moveBack(x,y,d) # 바라보는 방향을 유지한 채로 한 칸 후진을 하고
            continue # 2번으로 돌아간다.
    print(cnt)

H, W = map(int,stdin.readline().split())
y, x, d = map(int,stdin.readline().split())
area = [list(map(int,stdin.readline().split())) for _ in range(H)]
func(x,y,d)