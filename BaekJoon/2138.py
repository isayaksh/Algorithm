# 2138 전구와 스위치 < 실버 1 >
from sys import stdin, maxsize
from copy import deepcopy

MID = "mid"
END = "end"

def solution(N, default, target):
    answer = maxsize
    def createCase(default):
        case1 = default
        case2 = deepcopy(case1)
        case2[0], case2[1] = abs(case2[0]-1), abs(case2[1]-1)
        return case1, case2
    
    def switchOn(cases, idx, type):
        if type == MID:
            cases[idx-1],  cases[idx], cases[idx+1] = abs(cases[idx-1]-1),  abs(cases[idx]-1), abs(cases[idx+1]-1)
        elif type == END:
            cases[idx-1],  cases[idx] = abs(cases[idx-1]-1),  abs(cases[idx]-1)

    case1, case2 = createCase(default)
    cnt1, cnt2 = 0, 1

    for idx in range(1,N):
        if idx != N-1:
            if target[idx-1] != case1[idx-1]:
                switchOn(case1, idx, MID)
                cnt1 += 1
            if target[idx-1] != case2[idx-1]:
                switchOn(case2, idx, MID)
                cnt2 += 1
        else:
            if target[idx-1] != case1[idx-1]:
                switchOn(case1, idx, END)
                cnt1 += 1
            if target[idx-1] != case2[idx-1]:
                switchOn(case2, idx, END)
                cnt2 += 1

    if int(target[-1]) == case1[-1]:
        answer = cnt1
    if int(target[-1]) == case2[-1]:
        answer = min(answer, cnt2)

    return answer if answer != maxsize else -1

#input
N = int(stdin.readline())
default = list(map(int,list(stdin.readline().strip())))
target = list(map(int,list(stdin.readline().strip())))

# result
result = solution(N, default, target)
print(result)
