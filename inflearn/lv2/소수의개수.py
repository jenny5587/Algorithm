def count_t(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

n = int(input())
cnt = 0

for x in range(2, n+1):
    if count_t(x):
        cnt += 1
print(cnt)
