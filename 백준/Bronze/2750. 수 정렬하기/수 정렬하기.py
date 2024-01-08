N = int(input())
# 한 줄에 먼저 받기
bin = []
for i in range(N):
    bin.append(int(input()))
bin = sorted(bin)
for i in bin:
    print(i)