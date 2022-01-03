from sys import stdin, maxsize

N = int(stdin.readline())
H = [list(map(int,stdin.readline().split())) for _ in range(N)]

INF = maxsize
tmp = []

for i in range(3):
  A = [INF, INF, INF]
  A[i] = H[0][i]
  for j in range(1,N):
    tmp1 = H[j][0] + min(A[1], A[2])
    tmp2 = H[j][1] + min(A[0], A[2])
    tmp3 = H[j][2] + min(A[0], A[1])
    A[0], A[1], A[2] = tmp1, tmp2, tmp3
  A[i] = INF
  tmp.append(min(A))
print(min(tmp))