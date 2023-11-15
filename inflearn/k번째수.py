# k번째수 (자연수 N과 s부터 e번째까지 오름차순 정렬해서 k번째의 수)
import sys
sys.stdin=open("/K번째 수/in1.txt","rt")
#sys.stdin은 표준 입력 스트림을 나타내는 파일 유사 객체. 
#다른 입력 장치에 연결 받거나, 프로그램이 사용자로부터 입력을 받을 때 사용

st_to_int = int(input())
for i in range(st_to_int):
    N,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    # s가 두번째부터 시작하나, 인덱스로는 1번
    a=a[s-1:e]
    a.sort()
    print(f"#{a[k-1]}")
