# 2. 위에서 아래로 selection sort

n = int(input())
list = []
for i in range(n):
    num = int(input())
    list.append(num)

for i in range(len(list)):
    max_index = i
    for j in range(i+1, len(list)):
        if list[max_index] < list[j]:
            max_index = j
    list[i], list[max_index] = list[max_index], list[i]

print(list)
