a,b,c = map(int, input().split())

bin=[a,b,c]
#리스트 만든 후 sort하여 큰값으로 정렬
bin.sort(reverse=True)

if a==b==c:
    print(10000+(bin[0])*1000)
elif a==b or a==c or b==c:
    print(1000+(a if a==b or a==c else c)*100)
else:
    print(bin[0]*100)