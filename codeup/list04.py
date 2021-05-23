n = int(input())
badooklist = [[0 for i in range(19)] for j in range(19)]
points = []
for i in range(n):
    one = list(map(int, input().split()))
    points.append(one)

for point in points:
    badooklist[point[0]-1][point[1]-1] = 1

for badook in badooklist:
    for b in badook:
        print(b, end=' ')
    print('')
