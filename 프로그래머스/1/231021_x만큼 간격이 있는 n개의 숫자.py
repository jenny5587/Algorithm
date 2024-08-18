def solution(x, n):
    answer = []
    for i in range(x,x*n+x,x):
        answer.append(i)
    return answer


#cleancode
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        print(i)
        answer.append(x*i)
        # 곱하기로 품
    return answer
  
#check
#TypeError: 'int' object is not iterable -> answer가 리스트기 때문에 append했어야함
#첫번째 내가 푼 테스트는 성공하는데 자꾸 런타임 에러남..왜지ㅠ
