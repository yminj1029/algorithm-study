# 알파벳 찾기
import string
# 1. 알파벳 소문자로만 이루어진 단어 S
S = input()
# 알파벳 나열을 어떻게 할 것인가. 
# https://programmers.co.kr/learn/courses/4008/lessons/12729
# 숫자는 string.digits로 가능하다.0~9
# 2. 알파벳 별로 단어에 포함되어 있으면 처음 등장하는 위치를, 
# 3. 포함 되어 있지 않으면 -1
def find_alphabet(s):
    alphabet= string.ascii_lowercase
    for a in alphabet:
        if a in s:
            print(s.index(a),end=' ') #.index는 최솟값을 돌려준다.
        else :
            print(-1, end=' ')

find_alphabet(S)

# 더빠른 사람거 코드 : 알파벳범위를 아스키 코드를 이용해서 함.
data = list(input())
outPut = ''
for i in range(97, 123):
    ch = chr(i)
    if ch in data:
        outPut += (str(data.index(ch))+" ")
    else:
        outPut += "-1 "
print(outPut)
