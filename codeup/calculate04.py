# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

a = int(input())
print(~a)

num1, num2 = map(int, input().split())
print(num1 & num2)

num1, num2 = map(int, input().split())
print(num1 | num2)

num1, num2 = map(int, input().split())
print(num1 ^ num2)
