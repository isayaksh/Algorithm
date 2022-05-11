def solution(s):
    answer = 1000
    num = len(s)
    if num == 1: # 문자열의 길이가 1일 경우
        return 1 # 1 반환
    for i in range(1,num//2 + 1):
        tmp = list(map(''.join, zip(*[iter(s)]*i))) # 문자열을 N개 단위로 분할
        result = ["1", tmp[0]]
        count = 0
        for j in range(1,len(tmp)):
            if result[-1] == tmp[j]: # 현재 문자열이 이전 문자열과 같다면
                result[-2]  = str(int(result[-2]) + 1) # 현자 문자열의 개수 값 + 1
            else: # 현재 문자열이 이전 문자열과 다르다면
                result.append("1") # 현재 문자열의 개수 
                result.append(tmp[j]) # 현재 문자열 입력
        count = num % i # 전체 문자열을 N 크기 만큼 나눈 후 남은 문자열
        for r in result:
            if r != "1": count += len(r) # 생략한 "1" 이외의 문자열 길이의 합
        if answer > count: answer = count # 최소 문자열 길이 갱신
    return answer