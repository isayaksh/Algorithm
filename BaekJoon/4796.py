from sys import stdin
num = 1
while True:
  L, P, V = map(int,stdin.readline().split())
  if not L:
    break
  if V%P >= L:
    print("Case {}:".format(num),(V//P)*L+L)
  else:
    print("Case {}:".format(num),(V//P)*L+(V%P))
  num+=1