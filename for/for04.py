import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b= map(int,sys.stdin.readline().split())
    print(a+b)

# 나보다 빠른사람 코드
import sys
input = sys.stdin.readline
for i in range(int(input())):
    print(sum(map(int, input().split()))) # sum함수를 바로 사용했다. 이게 더 나은듯.