import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    print(i)

# 이문제는 input을 사용했을 때 빠르게 나왔다.
# sys.stdin.readline() : 반복문을 여러 줄로 입력을 받아야할때 사용한다.
# input() : 한두줄 입력받을 때 사용한다.