from sys import stdin

a = list(stdin.readline().split() for _ in range(15))
a.sort(key=lambda x : x[1])
print()
for c in a:
    print(' '.join(c))