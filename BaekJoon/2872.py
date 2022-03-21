# 2872 우리집에 도서관이 있어 < 실버 3 >
from sys import stdin
N = int(stdin.readline())
lst = []
for i in range(N):
  n = int(stdin.readline())
  lst.append(n)
  if n == N: 
    num = i # 가장 밑에 있어야할 책의 위치
result = N - num - 1 # 가장 밑에 있어야할 책의 위치보다 뒤에 있는 책들은 모두 앞으로 옮겨야 함
for i in range(num-1,-1,-1): # 가장 밑에 있어야할 책의 위치보다 앞에 있는 책들을 확인
  if N - 1 == lst[i]: # 현재 책이 바로 앞번(N-1)의 책이라면
    N -= 1 # 체크해야할 번호 - 1
  else:
    result += 1 # 정리값 + 1
print(result)