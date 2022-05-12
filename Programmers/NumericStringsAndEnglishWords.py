D = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
def solution(s):
    answer = 0
    word = "" # 문자열을 임시로 저장할 변수
    for char in s:
        # 현재 문자가 숫자라면
        if char.isdigit(): answer = answer * 10 + int(char)
        # 현재 문자가 숫자가 아니라면
        else:
            word += char # word에 현재 문자 추가
            if word in D: # word가 Dict에 존재한다면
                answer = answer * 10 + D[word]
                word = "" # word 초기화
    return answer