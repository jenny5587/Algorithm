import sys

sys.stdin=open("/Users/joungminhee/Desktop/pythonalgorithm_formac (1)/섹션 2/10. 점수 계산/in1.txt","rt")

n = int(input())

a = list(map(int, input().split()))

sum = 0
res = 0
for i in range(len(a)):
    if a[i] == 1:
        res += 1
        sum += res
    else:
        res = 0
print(sum)
