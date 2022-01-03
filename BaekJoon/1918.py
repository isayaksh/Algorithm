# 후위 표기식

from sys import stdin

form = list(stdin.readline().rstrip())

result=[]
stack=[]

for f in form:
  if f == '+' or f == '-':
    while stack and stack[-1] != '(':
      result.append(stack.pop())
    stack.append(f)
  elif f == '*' or f =='/':
    while stack and (stack[-1] == '*' or stack[-1] == '/') and stack[-1] != '(':
      result.append(stack.pop())
    stack.append(f)
  elif f == ')':
    while stack[-1] != '(':
      result.append(stack.pop())
    stack.pop()
  elif f == '(':
    stack.append(f)
  else:
    result.append(f)
while stack:
  result.append(stack.pop())
result = ''.join(result)
print(result)

