import sys
t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i+1,sum(map(int,sys.stdin.readline().split()))))


# lstrip : 왼쪽 공백이나 인자가 된 문자열의 모든 조합을 제거.
# rstrip: 인자가 없을 경우 오른쪽 공백 제거
# strip : 양쪽 문자열에 공백이나 인자가 된 문자열의 모든 조합을 제거

# sys.stdin.readline().rstrip까지 한 사람 코드가 더빨랏음
