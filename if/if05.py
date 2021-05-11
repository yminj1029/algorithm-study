H,M = map(int,input().split())

if M>=45:
    print(H, M-45)
else:
    if H > 0:
        print(H-1, M+15)
    elif H ==0:
        print(23, M+15)


# 다른 사람 것. -> h가 0일때랑 아닐때를 넣고 계산을 맨 앞에 해서 또하지 않음. 
h, m = map(int,input().split())

m -= 45
if m < 0:
    if h == 0:
        print(23,m+60)
    else:
        print(h-1,m+60)
else:
    print(h,m)