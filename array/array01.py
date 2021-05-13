n = int(input())
list = list(map(int, input().split()))
x = list[0:n]
print(min(x), max(x))

# 더 빠른 코드
a = int(input())
b = list(map(int,input().split()))
print(min(b), max(b))