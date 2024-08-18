def solution(array):
    answer = 0
    # array의 원소를 중복제거
    set_array = set(array)
    max_c = 0
      # set_array의 리스트에서 i개 추출
    for i in set_array:
      # array에서 현재 요소 i의 등장 횟수
        count = array.count(i)
        if max_c < count:
            max_c = count
            answer = i
        elif max_c == count:
            answer = -1
    return answer
