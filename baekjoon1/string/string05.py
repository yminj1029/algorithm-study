# 단어공부
# 대소문자로 이루어진 단어.
word = input()
# 가장 많이 쓰이는단어는 대문자로 출력 --> 처음부터 대문자로 바꾸기
W = word.upper()
# 가장 많이 쓰이는 단어는 대문자로 출력.
for w in W:
    cnt= W.count(w)
    print(cnt)