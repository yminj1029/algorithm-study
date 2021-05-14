# 문자열 반복
# 1. 문자열 S를 입력받는다.
# 2. 각 문자를 R번 반복한다.
# 3. 새 문자열 P를 만든다. 
# S는 alphanumeric

# 테스트 케이스의 개수
# T = int(input())
# for i in range(T):
#     n,s = input().split()
#     s = int(n)*s
#     result = ''.join(sorted(s))
#     print(result)
    
# 백준에서 sort가 안되는거 같다 : 바꾼답
T = int(input())
for i in range(T):
    # 반복할 수와 문자열 s입력
    n,S = input().split()
    P = ''
    for s in S :
        P += s*int(n) 
    print(P)