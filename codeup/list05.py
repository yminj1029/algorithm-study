# 바둑판 깔림
badookpan = []
for i in range(19):
    badook = list(map(int, input().split()))
    badookpan.append(badook)

# 십자 뒤집기 횟수
n = int(input())
points = []
# 십자 뒤집기 좌표가 횟수만큼 입력
for i in range(n):
    numlist = list(map(int, input().split()))
    points.append(numlist)

for point in points:
    for j in range(point[1]):
        for i in range(point[0]):
            if badookpan[i-2][j-2] == 1:
                badookpan[i-2][j-2] = 0
            elif badookpan[i-2][j-2]:
                badookpan[i-2][j-2] = 1

for badook in badookpan:
    for b in badook:
        print(b, end=' ')
    print('')
