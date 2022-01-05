# 1744 수 묶기 <골드 4>
from sys import stdin
lst1 = [] # 2이상의 양수를 저장할 리스트
lst2 = [] # 0과 음수를 저장할 리스트
result = 0 # 결과값
N = int(stdin.readline())
for _ in range(N):
  tmp = int(stdin.readline())
  if tmp > 1:
    lst1.append(tmp)
  elif tmp <= 0:
    lst2.append(tmp)
  elif tmp == 1: # 입력받은 값이 1일 경우 바로 더하기
    result+=1
lst1.sort()
lst2.sort(reverse=True)

while len(lst1)//2:
  result += (lst1.pop() * lst1.pop())
if lst1:
  result += lst1.pop()

while len(lst2)//2:
  result += (lst2.pop() * lst2.pop())
if lst2:
  result += lst2.pop()
print(result)