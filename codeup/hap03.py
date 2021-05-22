red, green, blue = map(int, input().split())

for r in range(red):
    for g in range(green):
        for b in range(blue):
            print(r, g, b)
print(red*green*blue)


num = int(input())
for i in range(1, num+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')
