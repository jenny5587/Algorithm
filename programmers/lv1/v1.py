#1부터 n까지 수를 번갈아 가며 n에 나누었을 때 나머지가 0인 수가 약수
#약수 구하기 문제

def solution(n):
    ans = 0
    for i in range(1, n+1):
        if n % i ==0:
            ans += i
    return ans

#cleancode
def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])
