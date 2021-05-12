n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)

# range함수를 사용해서 더 간단히 만든 다른 사람 코드
a = int(input())
x = range(1, a+1)
result = 0
for i in x:
    result += i
print(result)
