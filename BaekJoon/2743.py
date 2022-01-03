# ROT13

from sys import stdin

S = stdin.readline().rstrip('\n')

for s in S:
  if s.islower():
    s = ord(s)
    if s > 109:
      print(chr(s-13),end='')
    else:
      print(chr(s+13),end='')
  elif s.isupper():
    s = ord(s)
    if s > 77:
      print(chr(s-13),end='')
    else:
      print(chr(s+13),end='')
  else:
    print(s,end='')