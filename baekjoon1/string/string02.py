# 숫자의 합.
n = int(input())
a = input()
result = 0
for i in a[:n]:
    result += int(i)
print(result)