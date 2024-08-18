n, k = map(int, input().split())
a = list(map(int, input().split()))
# 중복은 1만 카운팅
res = set()
# 여러 조합을 비교해야하기때문에 3중구조
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            #set 자료구조는 append가 아닌 add
            res.add(a[i]+a[j]+a[m])
            #set은 리스트가 아니기때문에 sort가 되지않음
res=list(res)
res.sort(reverse=True)
# 0번부터 시작이므로 k-1
print(res[k-1])
