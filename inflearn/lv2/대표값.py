import sys

sys.stdin=open("in1.txt","rt")

n = int(input())
n_list = list(map(int, input().split()))
aveg = round(sum(n_list)/n)

min = 2147000000
# 가까운 값 찾기
# 인덱스와 값을 각각 대입
for i , x in enumerate(n_list):
    # 거리 구하기 = abs
    tmp = abs(x-aveg)
    # 점수에서 평균을 뺐을때 점수가 낮은것이 가장 가까움
    if tmp < min:
        min = tmp
        score = x
        res = i+1
    elif tmp == min:
        if x > score:
            score = x
            res = i+1
print(aveg, res)

### 최소값 구하기
arr = [3,4,5,7,8,2,1]
arrmin = float('inf')
for x in arr:
    if x < arrmin:
        arrmin = x
print(arrmin)
