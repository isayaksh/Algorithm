# 4949 균형잡힌 세상 <실버 4>
from sys import stdin
while True:
  S = stdin.readline().rstrip();
  if S == ".": # 입력받은 문자열이 "."인 경우
    break # 프로그램 종료
  B = [] # 괄호
  check = True # 
  for s in S:
    if s == '(' or s =='[':
      B.append(s)
    elif s == ')':
      if not B or B.pop() != '(':
        check = False
        break
    elif s == ']':
      if not B or B.pop() != '[':
        check = False
        break
  if check and not B:
    print("yes")
  else:
    print("no")      