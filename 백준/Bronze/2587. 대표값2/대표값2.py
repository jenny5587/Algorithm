numbers = [int(input()) for i in range(5)]
avg = int(sum(numbers) / len(numbers))
print(int(avg))
# 오름차순 정렬
numbers.sort()
# 길이 대비 중앙값 구하기
median = int(len(numbers) // 2)
print(numbers[median])