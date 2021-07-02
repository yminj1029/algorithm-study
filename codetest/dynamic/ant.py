# 개미 전사

n = int(input())
k = list(map(int, input().split()))

# dp 테이블 초기화

d = [0]*100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+k[i])

# 계산된 결과 출력
print(d[n-1])
