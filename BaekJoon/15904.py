from sys import stdin
N = list(stdin.readline().rstrip())
check = ['U','C','P','C']
cnum = 0
for n in N:
  if n == check[cnum]:
    cnum+=1
  if cnum == 4:
    print("I love UCPC")
    exit()
print("I hate UCPC")