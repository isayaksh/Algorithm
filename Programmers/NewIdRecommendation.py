def solution(new_id):
    answer = "."
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for word in new_id:
        if word.isdigit() or word.isalpha() or word in ["-", "_",]:
            answer += word
        # 3단계
        if word == "." and answer[-1] != ".":
            answer += word
    # 4단계
    answer = answer[1:]
    if answer:
        if answer[-1] == ".": answer = answer[:-1]
    # 5단계
    if not answer:
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".": answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while(len(answer) < 3):
            answer += answer[-1]
    return answer