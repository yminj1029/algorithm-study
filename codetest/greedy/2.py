# 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 중복가능 수 k
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()  # [6,5,4,4,2]
biggest = 0

for i in range(m):
    if((i+1) % (k+1) == 0):
        biggest += numbers[-2]
    else:
        biggest += numbers[-1]

print(biggest)


# book solution 01 -> for문으로 M이 커진다면 시간 초과가 될 수 있다.
# N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할때마다 1씩 빼기
    if m == 0:  # m이 0이라면 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)

# booksolution02 -> 반복되는 수열에 대해 파악

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)
result = 0
result += (count)*first  # 가장 큰 수 더하기
result += (m-count)*second  # 두번째로 큰 수 더하기

print(result)
