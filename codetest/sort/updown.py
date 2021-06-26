# 2. 위에서 아래로

n = int(input())
list = []
for i in range(n):
    num = int(input())
    list.append(num)

# sorted 함수
result = sorted(list, reverse=True)
print(result)

# sort 함수
list.sort(reverse=True)
print(list)

# 정렬이 수행된 결과 출력
for i in list:
    print(i, end=' ')
