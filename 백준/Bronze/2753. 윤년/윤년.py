n = int(input())

if (n % 400==0) or (n%100 != 0 and n %4==0):
    # 나머지 0은 배수
    print('1')
else:
    print('0')