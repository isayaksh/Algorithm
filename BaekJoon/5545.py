# 5545 최고의 피자 < 실버 3 >
from sys import stdin
N = int(stdin.readline()) # 토핑 종류의 수
A, B = map(int,stdin.readline().split()) # 도우 가격, 토핑 가격
C = int(stdin.readline()) # 도우의 열량
D = [] # 토핑의 열량
for _ in range(N):
    D.append(int(stdin.readline()))
D.sort(reverse=True)
sumD = C # 총 열량
price = A # 총 가격
for i in range(N):
    # 추가할 토핑의 1원당 열량이 현재 구성된 피자의1원당 열량 비율보다 크면
    if (sumD/price) < (D[i]/B): 
        sumD += D[i] # += 열량
        price += B # += 가격
print(sumD//price)