n, m = map(int, input().split())
# 리스트 0으로 해서 n+m 만큼 만듬
cnt = [0]*(n+m+10)
# for i in range(len(n)):
# int has no len()
for i in range(1, n+1):
    for j in range(1, m+1):
        # 주사위 눈의 합을 카운팅
        cnt[i+j]+=1
#빈도의 수 최대값 찾기
max = 0
for i in range(n+m+1):
    if cnt[i]> max:
        max =cnt[i]
# 최대값의 인덱스 찾기
for i in range(len(cnt)):
    if max == cnt[i]:
        print(i, end = ' ')
