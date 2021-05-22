n = int(input())
hap = 0
num = 0
while True:
    num += 1
    hap += num
    if hap >= n:
        print(hap)
        break

a, d, n = map(int, input().split())
print(a+d*(n-1))

a, r, n = map(int, input().split())
print(a*(r**(n-1)))
