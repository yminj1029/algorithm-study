n, m = map(int, input().split())

for i in range(1, n+1):
    for k in range(1, m+1):
        print(i, k)

c = input()
for num in range(1, 16):
    result = int(c, 16) * num
    print(f'{c}*{num:X}={result:X}')

num = int(input())
for i in range(1, num+1):
    if i % 10 != 0 and (i % 10) % 3 == 0:
        print('X', end=' ')
    else:
        print(i, end=' ')
