# 3687 성냥개비 < 골드 2 >
from sys import stdin

dp = [0,0,1,7,4,2,6,8,10] # 성냥개비 n개로 만들 수 있는 가장 작은 수의 배열
D = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8} # 성냥개비 2~7개로 만들 수 있는 가장 작은 수
for i in range(9,101):
    # 현재 성냥개비 수로 만들 수 있는 경우의 수 중에서 가장 작은 값을 dp에 추가
    element = min(dp[i-7]*10 + D[7], dp[i-6]*10 + D[6], dp[i-5]*10 + D[5], dp[i-4]*10 + D[4], dp[i-3]*10 + D[3], dp[i-2]*10 + D[2])
    dp.append(element)

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    # 홀수일 경우
    if n%2: MAX = '7' + '1' * ((n - 3) // 2)
    else: MAX = '1' * (n // 2)
    print(dp[n],MAX)