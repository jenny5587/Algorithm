def solution(n):
    answer = 0
    div = 6
    while div % n != 0:
        div += 6
    answer = div // 6
    return answer