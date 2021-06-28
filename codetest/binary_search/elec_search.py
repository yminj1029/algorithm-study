# 부품 찾기

# 가게의 부품
n = int(input())
store_goods = list(map(int, input().split()))
store_goods.sort()

# 손님 요청
m = int(input())
request_goods = list(map(int, input().split()))

# 각 부품이 존재하면 yes 존재하지 않으면 no를 출력한다.


def search_goods(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search_goods(array, target, start, mid-1)
    else:
        return search_goods(array, target, mid+1, end)


for i in range(m):
    result = search_goods(store_goods, request_goods[i], 0, n-1)
    if result is None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')
