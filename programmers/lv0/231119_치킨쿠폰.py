def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
         # chicken이 10보다 작아질 때까지
        chicken = div+mod
    return answer

#clean code
def solution(chicken):
    answer = 0
    while chicken >= 10:
      #divmod(chicken, 10): chicken을 10으로 나눈 몫과 나머지를 구함
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer
