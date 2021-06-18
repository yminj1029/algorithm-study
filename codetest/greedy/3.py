import time
import sys


# N : 행, M : 열의 개수
N, M = map(int, input().split())

number_list = []
numbers = []
number = 0
for n in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    number_list.append(min(numbers))

start = time.time()  # 시작 시간 저장
print(max(number_list))

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
