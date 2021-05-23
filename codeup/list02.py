num = int(input())
numlist = list(map(int, input().split()))
for i in range(1, num+1):
    print(numlist[num-i], end=' ')
