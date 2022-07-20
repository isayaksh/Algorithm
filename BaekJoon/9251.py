# 9251 LCS < 골드 5 >
from sys import stdin
def LCS(string1, string2):
    l1, l2 = len(string1), len(string2)
    dp = [[ 0 for _ in range(l1+1)] for _ in range(l2+1)]
    for y in range(1,l2+1):
        for x in range(1,l1+1):
            if string1[x-1] == string2[y-1]: # 문자가 같은 경우
                dp[y][x] = dp[y-1][x-1] + 1 # 현재 문자 이전의 LCS에 + 1
            else:
                dp[y][x] = max(dp[y-1][x], dp[y][x-1])
    return dp[l2][l1]
string1 = stdin.readline().strip()
string2 = stdin.readline().strip()
print(LCS(string1, string2))