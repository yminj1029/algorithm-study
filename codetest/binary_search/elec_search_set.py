# 집합 자료형 버전 부품 찾기

# 특정한 수가 한 번이라도 등장했는지를 검사하면 되므로 집합 자료형을 이용해서 문제를 해결 할 수 있다.
# set()함수는 집합 자료형을 초기화할 때 사용한다.
# 집합 자료형은 단순히 특정 데이터가 존재하는지 검사할 때에 매우 효과적으로 사용할 수 있다.

# N
n = int(input())

# 가게에 있는 전체 부품 번호를 입력받아서 집합 자료형에 기록
array = set(map(int, input().split()))
print(array)
# M
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
