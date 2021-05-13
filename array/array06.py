import sys
n = int(input())
cases = [sys.stdin.readline().rstrip() for x in range(n)]
for case in cases:   
    point = 0
    temp = 0
    for p in case :
        if p == 'O':
            temp += 1
            point += temp
        else :
            temp = 0
    print(point)
