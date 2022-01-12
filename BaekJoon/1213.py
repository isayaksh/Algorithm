# 1213 팰린드롬 만들기 <실버 4>
from sys import stdin
from collections import deque
string = list(stdin.readline().rstrip())
string.sort()

Front = []
Back = deque()
Tmp = None
num = len(string)
if num%2: #홀수
  i = 0
  while i < num-1: # 0 2 4 6
    if string[i] == string[i+1]:
      Front.append(string[i])
      Back.appendleft(string[i+1])
      i+=2
    else:
      if Tmp == None:
        Tmp = string[i]
        i+=1
      else:
        print("I'm Sorry Hansoo")
        exit()
  if i%2:
    if len(Tmp) == 1:
      Front.append(Tmp[0])
    else:
      print("I'm Sorry Hansoo")
      exit()
  else:
    Front.append(string[i])
else: # 짝수
  for i in range(0,num,2):
    if string[i] == string[i+1]:
      Front.append(string[i])
      Back.appendleft(string[i+1])
    else:
      print("I'm Sorry Hansoo")
      exit()
print(''.join(Front)+''.join(Back))