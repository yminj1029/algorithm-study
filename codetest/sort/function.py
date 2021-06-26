# sorted 소스 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)


# sort 소스코드
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr.sort()
print(arr)

# 정렬 라이브러리에서 key를 활용한 소스 코드

arr01 = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(arr01, key=setting)
print(result)
