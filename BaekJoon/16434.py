# BOJ 16434 드래곤 앤 던전
# https://www.acmicpc.net/problem/16434

from sys import stdin

def solution(N, Hatk, dungeon):
    HcurHP = 0
    HmaxHP = 0
    for type, atk, hp in dungeon:
        if type == 1: # 몬스터
            count = hp//Hatk - (0 if hp%Hatk else 1) # 몬스터 공격 횟수
            # 현재 체력(HcurHP)이 몬스터의 총 공격력(atk * count) 보다 적을 경우
            if HcurHP <= atk * count:
                HmaxHP += atk * count - HcurHP + 1
                HcurHP = 1
            # 현재 체력(HcurHP)이 몬스터의 총 공격력(atk * count) 보다 클 경우
            else:
                HcurHP -= atk * count
        if type == 2: # 포션
            Hatk += atk
            HcurHP = min(HcurHP + hp, HmaxHP)
    
    return HmaxHP

N, atk = map(int,stdin.readline().split())
dungeon = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, atk, dungeon)
print(res)