import sys
t = int(input())
for i in range(t):
    a,b= map(int,sys.stdin.readline().rstrip().split())
    print("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))