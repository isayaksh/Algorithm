# BOJ 19583 싸이버개강총회
# https://www.acmicpc.net/problem/19583

from sys import stdin

def hourToMinute(time):
    hour, minute = map(int,time.split(':'))
    return hour * 60 + minute

def getTimeLine(time):
    if 0 <= time <= S: return "ENTER"
    if E <= time <= Q: return "EXIT"
    return "NONE"

answer = 0
timeLines = dict()

# S(개강총회를 시작한 시간), E(개강총회를 끝낸 시간), Q(개강총회 스트리밍을 끝낸 시간)
S, E, Q = stdin.readline().split()
S, E, Q = hourToMinute(S), hourToMinute(E), hourToMinute(Q)

while True:
    chattingLog = stdin.readline().strip()

    if len(chattingLog) < 4: break

    time, name = chattingLog.split()
    timeLine = getTimeLine(hourToMinute(time))
    if name not in timeLines:
        if timeLine == "ENTER": timeLines[name] = [True, False]
        elif timeLine == 'EXIT': timeLines[name] = [False, True]
        else: timeLines[name] = [False, False]
    else:
        if timeLine == "ENTER": timeLines[name][0] = True
        elif timeLine == 'EXIT': timeLines[name][1] = True

for start, end in timeLines.values():
    if start and end:
        answer += 1

print(answer)