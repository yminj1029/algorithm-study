a = int(input())
print(bool(a))

b = bool(int(input()))
print(not b)

a, b = map(int, input().split())
print(bool(a) and bool(b))

a, b = map(int, input().split())
print(bool(a) or bool(b))

a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print((a and not b) or (not a and b))

print((not a and not b) or (a and b))

print(not a and not b)
