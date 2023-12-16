# k번째 약수
import sys
sys.stdin = open("/k번째 약수/in1.txt", "rt")
n,k = map(int, input().split())
# 갯수를 세어야 하니까
cnt = 0 
for i in range(1, n+1):
    # 약수 찾기
    if n% i == 0:
        cnt +=1
    if cnt ==k:
        print(i)
        break
else: 
    print(-1)


# 8,4 = 8
