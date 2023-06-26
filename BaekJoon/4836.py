# BOJ 4836 춤
# https://www.acmicpc.net/problem/4836

from sys import stdin

def solution(dances):
    rule = [False] * 6
    danceSet = set(dances)
    N = len(dances)

    # 1. dip은 jiggle을 춘 다음이나 다다음, 또는 twirl을 추기 전에 출 수 있다.
    for i in range(N):
        if dances[i] == 'dip':
            if (i > 0 and dances[i-1] == 'jiggle') or (i > 1 and dances[i-2] == 'jiggle'):
                continue
            if i < N-1 and dances[i+1] == 'twirl':
                continue
            dances[i] = 'DIP'
            rule[1] = True

    # 2. 모든 춤은 clap stomp clap으로 끝나야 한다.
    if N < 3 or (dances[-3], dances[-2], dances[-1]) != ('clap', 'stomp', 'clap'):
        rule[2] = True

    # 3. 만약 twirl을 췄다면, hop도 춰야한다.
    if 'twirl' in danceSet and 'hop' not in danceSet:
        rule[3] = True

    # 4. jiggle로 춤을 시작할 수 없다.
    if dances[0] == 'jiggle':
        rule[4] = True
    
    # 5. 반드시 dip을 춰야 한다.
    if 'dip' not in danceSet:
        rule[5] = True
    
    return [str(i) for i in range(1,6) if rule[i]]

while True:
    dances = stdin.readline().strip().split()

    if not dances: break

    problems = solution(dances)

    if not problems:
        print(f'form ok: ', end="")
    elif len(problems) == 1:
        print(f'form error {problems[0]}: ', end="")
    else:
        print(f'form errors {", ".join(problems[:-1])} and {problems[-1]}: ',end="")

    print(" ".join(dances))