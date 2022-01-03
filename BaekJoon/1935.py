#후위 표기식2

from sys import stdin

stack=[]
dic={}
alpha=65


N = int(stdin.readline())
form = stdin.readline().rstrip()

for i in range(N):
  value = int(stdin.readline())
  dic[chr(alpha)] = value
  alpha+=1

for f in form:
  if f == '+':
    b=stack.pop()
    a=stack.pop()
    stack.append(a+b)
  elif f == '-':
    b=stack.pop()
    a=stack.pop()
    stack.append(a-b)
  elif f == '*':
    b=stack.pop()
    a=stack.pop()
    stack.append(a*b)
  elif f == '/':
    b=stack.pop()
    a=stack.pop()
    stack.append(a/b)
  else:
    stack.append(int(dic[f]))

print("{:.2f}".format(stack[0]))

