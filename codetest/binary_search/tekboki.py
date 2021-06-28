# 떡볶이 떡 만들기
# 파라메트릭 서치 유형의 문제이다. : 범위내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제

# 떡의 개수, 떡의 길이
n, m = map(int, input().split())

# 떡의 개별 높이
array = list(map(int, input().split()))

# 재귀보다 반복문이 더 간결하다.
# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
