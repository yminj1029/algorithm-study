# 상하 좌우 문제

n = int(input())
x, y = 1, 1
# 명령 입력
command = list(input().split())

# L은 왼쪽에서 한 칸 이동
# R은 오른쪽에서 한 칸 이동
# U는 위로 한칸 이동
# D는 아래로 한 칸 이동.

for com in command:
    if com == 'L':
        if y-1 != 0:
            y = y-1
        else:
            continue
    elif com == 'R':
        y = y+1
    elif com == 'U':
        if x-1 != 0:
            x = x-1
        else:
            continue
    elif com == 'D':
        x = x+1


print(x, y)


# book

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y+dy[i]
        # 공간에서 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
print(x, y)
