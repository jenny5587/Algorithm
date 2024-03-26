x = int(input())
n = int(input())

sum = 0
# n개의 줄에는 각 물건의 가격 a와 개수 b가 주어진다
# 그말은 즉, n개의 줄 수만큼 반복한다
for i in range(n):
    a,b = map(int, input().split())
    sum += a*b
if x == sum:
    print('Yes')
else:
    print('No')
