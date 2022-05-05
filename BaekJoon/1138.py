# 1138 한 줄로 서기 < 실버 2 >
from sys import stdin
N = int(stdin.readline())
leftSide = [0] + list(map(int,stdin.readline().split()))
result = []
# 키가 가장 큰 사람부터 가장 작은 사람까지
for i in range(N,0,-1):
  result.insert(leftSide[i],str(i)) # 왼쪽에 존재하는 사람 수 위치에 insert()
print(" ".join(result))