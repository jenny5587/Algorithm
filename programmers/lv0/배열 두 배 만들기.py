def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

#cleancode
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))
