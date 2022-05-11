def solution(record):
    answer = []
    D = {} # { key : uid, value: 닉네임 }
    idx = 0
    # 닉네임 갱신
    for r in record:
        data = r.split()
        if data[0] == "Enter" or data[0] == "Change": 
            D[data[1]] = data[2]
    # 채팅방 출입 메시지
    for r in record:
        data = r.split()
        if data[0] == "Enter":
            answer.append(D[data[1]] + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(D[data[1]] + "님이 나갔습니다.")
    return answer