num = 1
while (num != 0):
    num = int(input())
    if num != 0:
        print(num)

number = int(input())
while True:
    if number == 0:
        break
    print(number)
    number -= 1

number = int(input())
while True:
    number -= 1
    print(number)
    if number == 0:
        break

alpha = ord('a')
alphabet = ord(input())
while True:
    if alpha > alphabet:
        break
    print(chr(alpha), end=' ')
    alpha += 1

num1 = int(input())
for i in range(num1+1):
    print(i)
