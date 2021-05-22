n = int(input())
hap = 0
for i in range(1, n+1):
    if i % 2 == 0:
        hap += i

print(hap)


while True:
    c = input()
    print(c)
    if c == 'q':
        break

n = int(input())
hap = 0
for i in range(1, n+1):
    hap += i
    if hap >= n:
        print(i)
        break
