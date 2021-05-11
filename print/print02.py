# 맵 객체 : 리스트처럼 변환해줌 맵만 써서 프린트하면 주소값을 준다.
plus= map(int, input().split())
print(sum(plus))

minus = list(map(int, input().split()))
print(minus[0]-minus[1])

multiply = list(map(int, input().split()))
print(multiply[0]*multiply[1])

division = list(map(int, input().split()))
print(division[0]/division[1])