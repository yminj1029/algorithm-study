import sys
list= []
for i in range(10):
    num = int(sys.stdin.readline().rstrip())
    list.append(num%42)
result = set(list)
print(len(result))

# set 이용하면 집합은 중복을 제거한다.
#for 문 이용
# my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
# new_list = []
# for v in my_list:
#     if v not in new_list:
#         new_list.append(v)
# print(new_list)
# 출력된 값 ['A', 'B', 'C', 'D', 'E']