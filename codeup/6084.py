h, b, c, s = map(int, input().split())

print(f'{h*b*c*s/8/1024/1024:0.1f} MB')

w, h, b = map(int, input().split())
print(f'{w*h*b/8/1024/1024:0.2f} MB')
