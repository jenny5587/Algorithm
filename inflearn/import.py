import sys
# sys.stdin=open("/Users/joungminhee/Desktop/pythonalgorithm_formac (1)/섹션 2/5. 정다면체/in1.txt","rt")

# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
# 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다

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