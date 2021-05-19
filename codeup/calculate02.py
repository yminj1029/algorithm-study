# 정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
# 가장 오른쪽에 있는 1비트는 사라진다.
a = int(input())
print(a << 1)

num1, num2 = map(int, input().split())
print(num1 << num2)

n1, n2 = map(int, input().split())
print(n1 < n2)

n1, n2 = map(int, input().split())
print(n1 == n2)

n1, n2 = map(int, input().split())
print(n1 <= n2)

n1, n2 = map(int, input().split())
print(n1 != n2)