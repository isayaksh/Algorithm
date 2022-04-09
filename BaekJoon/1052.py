# 1052 물병 <실버 1>
from sys import stdin
N, K = map(int,stdin.readline().split())
D=[]
count = 1
result = 0
while(N): # N의 값을 2의 제곱수 중 가장 큰 값으로 분리하여 리스트에 저장
  if N == 1: # 현재 N의 값이 1일 경우
    D.append(1)
    break
  elif count >= N: # 현재 N의 값이 count 보다 작거나 같은 경우
    if count > N:
      count //= 2
    N -= count
    D.append(count)
    count = 1
  else: # 현재 N의 값이 count보다 클 경우
    count *= 2

while (len(D) > K): # 현재 배열의 원소의 수가 K보다 작거나 같을 때까지 반복
  if len(D) > 1 and D[-2] == D[-1]: # 현재 배열의 마지막 원소 2개가 같을 경우
    D.pop()
    D.append(2*D.pop())
    continue
  tmp1 = D.pop()
  tmp2 = D.pop()
  result += tmp2 - tmp1
  D.append(tmp2*2)
print(result)