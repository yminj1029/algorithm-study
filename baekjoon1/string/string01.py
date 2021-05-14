# 파이썬 아스키 코드 -> 문자/ 문자 -> 아스키 코드 변환
# chr() : 숫자에 맞는 아스키 코드를 반환한다.
# ord() : 문자에 맞는 아스키 코드를 반환해준다. 

def asc(n):
    if type(n) == str:
        result = ord(n)
    else:
        result = chr(int(n))
    return result

a= input()
print(asc(a))