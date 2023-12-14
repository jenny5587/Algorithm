import sys

sys.stdin=open('','rt')

N = int(input())

# 상금 초기화
res =0
for i in range(N):
    tmp = input().split()
    #가장 큰 숫자 찾기
    tmp.sort()
    a,b,c = map(int, tmp)
    # 같은 눈이 3개
    if a == b and b==c:
        money = 10000+a*1000
    # 같은 눈이 2개 / 정렬을 했기 때문에 a보다 작을 수가 없음
    elif a ==b or a==c:
        money = 1000+a*100
    elif b == c:
        money = 1000+b*100
    else:
        money = c*100
    if money>res:
        res = money
print(res)
