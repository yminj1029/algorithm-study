num = int(input())
print('%x' % num)  # x는 16진수 hex

num1 = int(input())
print('%X' % num1)  # 16진수 대문자는 대문자로

num2 = int(input(), 16)  # 바로 16진수로 인식시키는 법
print('%o' % num2)  # 8진수는 octo o

num3 = ord(input())  # ord(문자)는 어떤 문자의 순서 위치 값을 의미한다. 문자를 10진수로 변환한 값
print(num3)  # 숫자를 아스키 코드로 : chr(숫자)
