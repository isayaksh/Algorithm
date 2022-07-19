# 14916 거스름돈 < 실버 5 >
from sys import stdin

def NumberOfChanges(n):
    lst = [0, -1, 1, -1, 2, 1, 3, 2, 4] # 거스름돈 1 ~ 8 까지의 경우
    for _ in range(9,n+1): # 거스름돈 9 ~ n 까지의 경우
        # 현재 보다 2원 적거나 5원 적은 경우에서 코인 1개를 더했을 때
        lst.append(min(lst[-2]+1,lst[-5]+1)) 
    return lst[n]

n = int(stdin.readline())
print(NumberOfChanges(n))