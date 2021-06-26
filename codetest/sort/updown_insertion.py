# 2. 위에서 아래로 insertion sort

n = int(input())
list = []
for i in range(n):
    num = int(input())
    list.append(num)

for i in range(1, len(list)):
    for j in range(i, 0, -1):
        if list[j] > list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break

print(list)
