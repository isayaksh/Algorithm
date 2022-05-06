# 1092 배 < 골드 5 >
from sys import stdin
N = int(stdin.readline())
cranes = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
boxes = list(map(int,stdin.readline().split()))

cranes.sort(reverse=True) # 크레인 내림차순으로 정렬
boxes.sort(reverse=True) # 박스 내림차순으로 정렬
result = 0
if boxes[0] > cranes[0]: # 제일 무거운 박스가 크레인 무게 제한보다 크다면
  print(-1)
  exit() # 프로그램 종료
while boxes: 
  for crane in cranes: # 모든 크레인
    for i in range(len(boxes)):
      if crane >= boxes[i]: # 현재 박스가 크레인 무게 제한보다 작거나 같다면
        boxes.pop(i) # 박스 제거
        break
  result += 1 # 모든 크레인 박스 이동 후 1분 추가
print(result)  