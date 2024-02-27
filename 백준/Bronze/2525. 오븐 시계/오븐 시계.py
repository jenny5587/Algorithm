h,m = map(int, input().split())
plus = int(input())

h += plus // 60
# // -> 나눗셈 먼저 진행한 뒤 정수만 반환
m += plus % 60
if m >=60:
    h +=1
    m = m%60
if h >=24:
    h -=24
print(h,m)