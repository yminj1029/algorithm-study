num = int(input())
print(num*(-1))

c = ord(input())
print(chr(c+1))

num1, num2 = map(int, input().split())
print(num1-num2)

f1, f2 = map(float, input().split())
print(f1*f2)

w, cnt = input().split()
print(w*int(cnt))

n = int(input())
s = input()
print(n*s)

n1, n2 = map(int, input().split())
print(n1**n2)

f1, f2 = map(float, input().split())
print(f1**f2)

i1, i2 = map(int, input().split())
print(i1//i2)

t1, t2 = map(int, input().split())
print(t1 % t2)

number = float(input())
print(f'{number:0.2f}')

fn1, fn2 = map(float, input().split())
print(f'{fn1/fn2:0.3f}')

number1, number2 = map(int, input().split())
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1//number2)
print(number1 % number2)
print(f'{number1/number2:0.2f}')


a, b, c = map(int, input().split())
s = a + b + c
print(f'{s} {s/3:0.2f}')
