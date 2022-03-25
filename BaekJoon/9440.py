# 9440 숫자 더하기 < 실버 3 >
from sys import stdin
while True:
  N = list(map(int,stdin.readline().split()))
  if N[0] == 0: # 프로그램 종료
    break
  N = sorted(N[1:]) # 정렬
  A, B = "", "" # 두 숫자 문자열
  zeroCount = 0 # 0의 갯수
  TF = True
  for num in N:
    if num == 0: # 0일 경우
      zeroCount += 1 # 0의 갯수 + 1
      continue # 다음 반복문 시작
    # 각 숫자 문자열에 값을 차례로 추가
    if TF:
      A += str(num)
      TF = False
    else:
      B += str(num)
      TF = True
  for _ in range(zeroCount): # 0의 갯수에 맞추어 각 수의 두번째 자리에 0 추가
    if len(A) == len(B):
      A = A[0] + '0' + A[1:]
    else:
      B = B[0] + '0' + B[1:]
  print(int(A)+int(B))