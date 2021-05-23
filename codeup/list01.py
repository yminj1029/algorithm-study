num = int(input())
numlist = list(map(int, input().split()))
# 1~23번까지 있고 번호는 무작위로 불려짐. 몇번까지인지 숫자 출력.

for i in range(1, 24):
    if numlist.count(i):
        print(numlist.count(i), end=' ')
    else:
        print(0, end=' ')
