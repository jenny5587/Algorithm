def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            # list -> append
            answer.append(i)
    return answer

#cleancode
def solution(n):
    return [i for i in range(1, n+1, 2)]

#리스트 컨프리핸션이란?
# 새로운_리스트 = [표현식 for 요소 in 이터러블 if 조건]
