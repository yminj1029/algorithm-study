# 왕실의 나이트

# 1. 수평 2칸 이동, 수직 1칸 이동 +2
# 2. 수직 2칸 이동, 수평 1칸 이동
# 정원 밖으로는 나갈 수 없다.

# 입력 받는 위치
point = input()
su = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

garo = ord(point[0])
sero = int(point[1])

# print(ord('a')) ->97
# print(ord('h')) ->104

count = 0
for s in su:
    if garo+s[0] < 97 or garo+s[0] > 104:
        continue
    if sero+s[1] < 1 or sero+s[1] > 8:
        continue
    else:
        count += 1
print(count)


# book

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-int(ord('a')))+1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column+step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
