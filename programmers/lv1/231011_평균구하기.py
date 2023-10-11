# arr배열의 평균구하기
def solution(arr):
    ans = 0
    for i in arr:
        ans += i
        answer = ans / len(arr)
    return answer

#clencode
def solution(arr):
    return sum(arr) / len(arr)
# sum함수를 쓰면 쉽게 풀릴 문제..
