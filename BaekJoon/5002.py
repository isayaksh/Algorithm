# 5002 도어맨 < 실버 1 >
from sys import stdin
X = int(stdin.readline())
people = list(stdin.readline().rstrip())
num = len(people)
total = 0 # 입장 인원 수
count = 0 # 
idx = 0
while(idx <num):
  if people[idx] == 'W':
    if count > -X:
      count -= 1
    else:
      if idx + 1 < num and people[idx+1] == 'M':
        idx += 1
        total += 1
      else:
        break
  elif people[idx] == 'M':
    if count < X:
      count += 1
    else:
      if idx+1 < num and people[idx+1] == 'W':
        idx += 1
        total += 1
      else:
        break
  idx += 1
  total += 1
print(total)