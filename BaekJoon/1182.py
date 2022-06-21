# 1182 부분 수열의 합  < 실버 2 >
from itertools import combinations
from sys import stdin

N, S = map(int,stdin.readline().split())
sequence = list(map(int,stdin.readline().split()))
cnt = 0
for i in range(1,N+1):
    for num in combinations(sequence,i): # 모든 조합의 수
        if S == sum(num): cnt += 1 # 조합의 합이 S와 같을 경우 cnt += 1
print(cnt)
# from sys import stdin
# cnt = 0
# def func(idx, sum):
#     global cnt
#     if idx >= N: return
#     sum += sequence[idx]
#     if sum == S: cnt += 1
#     func(idx+1, sum - sequence[idx])
#     func(idx+1, sum) 
# N, S = map(int,stdin.readline().split())
# sequence = list(map(int,stdin.readline().split()))
# func(0,0)
# print(cnt)