import sys

# 딕셔너리 사용버전
dic = {}
for i in range(9):
    x = int(sys.stdin.readline().rstrip())
    dic[x] = i+1
print(max(dic.keys()),dic[max(dic.keys())])

#리스트 사용버전
# list = []
# for i in range(9):
#     x = int(sys.stdin.readline().rstrip())
#     list.append(x)

# max_num = max(list)
# print(max_num, list.index(max_num)+1)
