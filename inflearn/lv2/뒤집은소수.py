# 첫 줄에 자연수의 개수 입력
N = int(input())
# 원소들 리스트화
a = list(map(int,input().split()))
# reverse는 list타입에서 제공하는 함수
def reverse(x):
    # [::-1]의 슬라이싱 표기법을 이용하면 시퀀스(문자열이나 리스트 등)의 원소 순서를 역순으로 만듬
    return int(str(x)[::-1])

# 소수 확인 코드
def isprime(x):
    if x == 1:
        return False
    # 1과 자기 자신 정수를 포함하지 않기 위해, 16을 예로 들때 2,8도 되기때문에 //2로 진행
    for i in range(2, x//2+1):
        if (x % i == 0):
            return False
    return True

for i in a:
    rev = reverse(i)
    # int is no attribute reverse, str으로 진행
    if isprime(rev):
        print(rev, end=' ')
