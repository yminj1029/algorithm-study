list = list(map(int,input().split()))

print(list[0]+list[1])
print(list[0]-list[1])
print(list[0]*list[1])
print(int(list[0]/list[1]))
print(list[0]%list[1])

# 굳이 리스트로 만들지 않고 두개의 변수로 받았다.
A,B = map(int,input().split())
print(A+B, A-B, A*B, A//B, A%B, sep='\n')	
# sep='\n'로 줄바꿈

# print 옵션
# sep(seperation) : 영단어 그대로 분리하여 출력한다. 분리(구분자)할 문자를 넣을 수 있다 sep=''
# end : 그 뒤의 값과 이어서 출력한다. end=' '
# format : 특정 문자를 넣어서 프린트 할 수 있다.
#             %s, %d, %f
# Escape  \n : 줄바꿈
#         \ㅅ : 탭
#         \\ : \ 출력
#         \' : 작은 따옴표 출력
#         \b : 백스페이스