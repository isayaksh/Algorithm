from sys import stdin
B = list(stdin.readline().rstrip())
result = []
cnt = 0
for b in B:
  if b == 'X':
    cnt +=1
  else:
    if cnt//4:
      result.append("AAAA"*(cnt//4))
      cnt %= 4
    if cnt//2:
      result.append("BB")
      cnt %= 2
    if cnt:
      print(-1)
      exit()
    result.append('.')
if cnt//4:
      result.append("AAAA"*(cnt//4))
      cnt %= 4
if cnt//2:
  result.append("BB")
  cnt %= 2
if cnt:
  print(-1)
  exit()
print(''.join(result))