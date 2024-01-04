# 앞에서 읽거나 뒤로 읽거나 같으면 회문 문자열이라고 한다

import sys

sys.stdin=open("/Users/joungminhee/Desktop/pythonalgorithm_formac/섹션 3/1. 회문 문자열 검사/in1.txt","rt")

N = int(input())

for i in range(N):
    n = input()
    n = n.upper()
    s = len(n)
    for j in range(s//2):
        if n[j]!= n[-1-j]:
            print('#%d No' %(i+1))
            break
    else:
            print('#%d YES' %(i+1))

#for ~ else~ 구문
#for문이 break 없이 정상적으로 종료되면 다음 else 구문을 실행, for문이 중간에 break를 당해 종료되면 else 구문을 하지 않는다.