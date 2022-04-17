# 12927 배수 스위치 < 실버 4 >
from sys import stdin
Lights = [0] + list(stdin.readline().rstrip())
count = 0 # 스위치 동작 횟수
num = len(Lights) # 전구 갯수
for i in range(1, num):
  if Lights[i] == 'Y': # i 위치의 전구가 켜져있다면
    count += 1 # 스위치 동작 횟수 + 1
    for j in range(i,num,i): # i의 배수 전구의 값 변환
      if Lights[j] == 'Y': Lights[j] = 'N'
      else: Lights[j] = 'Y'
print(count)