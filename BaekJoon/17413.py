# 단어 뒤집기2

from sys import stdin

sentence = stdin.readline().rstrip()
count=len(sentence)
stack = []

for i in range(count):
  if sentence[i] == '<':
    if stack:
      output = ''.join(stack)
      print(output[::-1],end='')
    stack= ['<']
  elif sentence[i] == '>':
    output = ''.join(stack)
    print(output,end='>')
    stack=[]
  elif sentence[i] == ' ' and stack[0] != '<':
    if stack:
      output = ''.join(stack)
      print(output[::-1],end=' ')
      stack=[]
  else:
    stack.append(sentence[i])
  if i == count-1 and stack:
    output = ''.join(stack)
    print(output[::-1],end='')