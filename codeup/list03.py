num = int(input())
numlist = list(map(int, input().split()))

numlist.sort()
print(numlist[0])
minnum = numlist[0]
for i in range(num):
    if numlist[i] <= minnum:
        minnum = numlist[i]

print(minnum)
