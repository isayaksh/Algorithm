# 2798 블랙잭 < 브론즈 2 > 
from itertools import combinations
from sys import stdin
N, M = map(int,stdin.readline().split())
Cards = map(int,stdin.readline().split())
sub = M
for cards in combinations(Cards,3): # 3장의 카드로 생성 가능한 모든 조합
    tmp = M - sum(cards)
    if tmp < 0: continue # 3장의 카드의 합이 M 보다 크다면 continue
    sub = min(sub, tmp)
print(M - sub)