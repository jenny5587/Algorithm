def solution(record):
    answer = []
    user = {}
    for rec in record:
        r = rec.split()
        act = r[0]
        uid = r[1]
        if act in ["Enter","Change"]:
            name = r[2]
            user[uid] = name
    for ans in record:
        a = ans.split()
        act = a[0]
        #uid= a[1]이 없어서 계속 오류 났음..정의하지 않는다면, 마지막 요소의 사용자 id만을 사용하기 때문에, 다시 재정의 필요성있음
        uid = a[1]
        if act =="Enter":
            answer.append(f"{user[uid]}님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(f"{user[uid]}님이 나갔습니다.")
    return answer
