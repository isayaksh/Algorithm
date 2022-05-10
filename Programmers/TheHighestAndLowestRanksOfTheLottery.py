def solution(lottos, win_nums):
    count = 7 # 순위
    for lotto in lottos:
        if lotto in win_nums: # 구매한 번호가 당첨번호와 같다면
            count -= 1 # 순위 + 1
    zero = lottos.count(0) # 알아볼 수 없는 번호 수
    answer = [ min(count-zero, 6), min(count, 6) ] # 최고 순위, 최저 순위
    return answer