import math

def solution(price):
    answer = 0
    # 소수점버리기
    if price >= 100000 and price <= 299999:
        answer = math.floor(price * 0.95)
    elif price >= 300000 and price <= 499999:
        answer = math.floor(price * 0.9)
    elif price >= 500000:
        answer = math.floor(price * 0.8)
    else:
        answer = price
    return answer
