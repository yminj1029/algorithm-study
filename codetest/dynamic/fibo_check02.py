# 피보나치 보텀업 방식

# 앞에서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

# 코딩 테스트에서 재귀함수를 이용하는 탑다운 방식보다는 보텀업 방식으로 구현하는 것을 권장한다.
# 시스템 상 재귀함수의 스택 크기가 한정되어 있을 수 있기 때문이다.
