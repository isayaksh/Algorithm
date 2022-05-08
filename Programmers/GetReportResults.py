def solution(id_list, report, k):
    answer = [0] * len(id_list) # answer 초기화
    report = set(report) # set()을 이용한 중복 신고 제거
    blackList = {x:0 for x in id_list} # 유저별 신고 횟수를 기록한 dict
    
    # 각 유저별 신고 횟수 Count
    for r in report:
        blackList[r.split()[1]] += 1
    
    # 각 유저별 메일 받은 횟수 Count
    for r in report:
        a, b = r.split() # 신고자, 신고 대상자
        if blackList[b] >= k: # 신고 대상자가 정지 기준 이상의 신고 횟수가 누적되었다면
            answer[id_list.index(a)] += 1 # 신고자의 메일 횟수 + 1
            
    return answer