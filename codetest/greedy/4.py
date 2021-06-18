# 99page 1이 될 때까지

n, k = map(int, input().split())
cnt = 0
while True:
    if n == 1:
        print(cnt)
        break
    if n % k == 0:
        n = n//k
        cnt += 1
    else:
        n = n-1
        cnt += 1

# N의 값을 줄이기 위해 최대한 많이 나눈다.
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
