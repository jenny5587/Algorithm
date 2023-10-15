#순열의 조합
def solution(babbling):
    answer = 0
    babb_list = ["aya","ye","woo","ma"]
    #babbling에서 한개씩 꺼낸 뒤
    for bab in babbling:
        #babb_list에서 꺼낸것과 비교해서 맞다면 조합 따져서 '_'로 바꾸기
        for i in babb_list:
            bab = bab.replace(i,'_')
        # _가 들어간 것들은 모두 공백으로 처리
        bab=bab.replace('_','')
        print(bab)
       #bab에 들어간 것들 중 공백이 있다면 그것을 cnt
        if len(bab) == 0:
            answer +=1
    return answer
#add
from itertools import permutations
def solution(babbling):
    answer=0
    babb_list = ['aya','ye','woo','ma']
    plus = []
    for i in range(1,len(babb_list)+1):
        #가능한 모든 순열을 생성하는 이터레이터
        for j in permutations(babb_list,i):
            # 문자열을 결합하는 메서드
            plus.append(''.join(j))
            print(plus)
        #babbling의 i가 plus의 i라면
    for i in babbling:
        if i in plus:
            answer += 1
    return answer
    
#clencode
import re #정규표현식 모듈
def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    # ^ : 문자열 시작
    # (aya|ye|woo|ma)
    # + : 패턴이 하나 이상 반복
    # $ : 문자열의 끝을 의미
    answer=0
    for e in babbling:
        if regex.match(e):
            answer+=1
    return answer
