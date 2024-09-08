# TypeError: 'int' object is not callable -> del max surve


# a = [3, 29, 38, 12, 57, 74, 40, 85, 61]
# print(max(a))
# print(a.index(max(a))+1)

bin = []
for i in range(9):
    num = int(input())
    bin.append(num)

print(max(bin))
print(bin.index(max(bin))+1)