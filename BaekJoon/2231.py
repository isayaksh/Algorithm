# 2231 분해합 < 브론즈 2 >
from sys import stdin
N = int(stdin.readline())
for num in range(1, N+1): # 1 ~ N 까지의 모든 수
    tmp = num + sum(list(map(int, str(num)))) # 분해합 결과
    if tmp == N: # 분해합의 결과가 N과 같다면
        print(num)
        exit()
print(0)