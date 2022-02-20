from sys import stdin
zero = [1,0]
one = [0,1]
for i in range(2,41):
  zero.append(zero[i-1]+zero[i-2])
  one.append(one[i-1]+one[i-2])

T = int(stdin.readline())
for _ in range(T):
  N = int(stdin.readline())
  print(zero[N],one[N])