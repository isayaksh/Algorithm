# 17828 문자열 화폐 < 골드 5 >
from sys import stdin
N, X = map(int,stdin.readline().split())
if X > N * 26 or N > X:
    print("!")
else:
    V = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ" # V[가치(1 ~ 26)] = 화폐(A ~ Z)
    result = [1] * N # N 크기의 문자열
    X -= N # N 크기 만큼 가치 1만큼을 투자하고 남은 가치
    idx = N - 1 # 문자열의 마지막 인덱스
    while X > 25: # 가치의 값이 화폐의 최대값인 'Z' 이상이 남았을 때
        result[idx] += 25 # 현재 문자열에 'Z' 의 가치인 26 할당
        X -= 25 # 가치 값에 25 차감
        idx -= 1 # 다음 인덱스로 이동
    result[idx] += X 
    for r in result:
        print(V[r],end="")