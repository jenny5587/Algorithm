T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    sum_a = 0
    min_a = float('inf')
    # 무한대값으로 초기화 -> 0으로 하면 어떤값보다 작기 때문에 최솟값이 반환되지 않음
    for j in a:
        if j % 2 == 0:
            sum_a += j
            min_a = min(min_a, j)
            #min(min_a, i)은 두 값을 비교하여 작은 값을 반환하는 함수
    print(sum_a,min_a)