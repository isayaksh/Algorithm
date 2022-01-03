# 문자열 분석

from sys import stdin

while True:

  N = stdin.readline().rstrip('\n')

  if not N:
    break

  l,u,d,s = 0,0,0,0

  for n in N:
    if n.islower():
      l+=1
    elif n.isupper():
      u+=1
    elif n.isdigit():
      d+=1
    elif n.isspace():
      s+=1
  print(l,u,d,s)