def solution(n):
    add = 0
    for i in str(n):
        # print(i)
        add += int(i)
    return add

#cleancode
def sum_digit(number):
    return sum(map(int, str(number)))
# map(int, str(number))는 해당 문자열을 순회하면서 각 문자(자릿수)를 정수로 변환.
  결과적으로 숫자의 각 자릿수를 정수 리스트로 얻음
