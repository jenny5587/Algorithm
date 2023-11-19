### 중앙값 구하기

def solution(array):
    answer = 0
    #일단, 배열을 먼저 오름차순으로 정렬
    array.sort()
    # 배열 길이 / 2 해주면 중앙값을 구할 수 있다
    center = len(array) //2 
    # 인덱스로 array의 중앙값을 구함
    answer = array[center]

#cleancode
def solution(array):
    return sorted(array)[len(array) // 2]
