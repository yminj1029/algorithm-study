subject = int(input())
points = list(map(int,input().split()))
result = []
for point in points :
    result.append(point/max(points)*100)
avg = sum(result)/len(result)
print(avg)

# 다른사람 코드 리스트 컴프리헨션을 사용해서 더 빠르게 계산을 했다. 
# import sys
# n=int(sys.stdin.readline().rstrip())
# g=[int(x) for x in sys.stdin.readline().rstrip().split()]
# m=max(g)
# l=[]
# for i in g:
#     i=i/m*100
#     l.append(i)
# print(sum(l)/n)