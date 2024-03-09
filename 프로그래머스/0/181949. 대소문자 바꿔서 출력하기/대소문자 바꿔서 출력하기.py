str = input()
r =""
for i in str:
    # 소문자 판별 함수
    if i.islower():
        r += i.upper()
    else:
        r += i.lower()
print(r)