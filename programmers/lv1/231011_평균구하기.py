def solution(arr):
    ans = 0
    for i in arr:
        ans += i
        answer = ans / len(arr)
    return answer
