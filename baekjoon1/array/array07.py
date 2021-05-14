import sys
test_cnt = int(input())

for i in range(test_cnt):
    student_score= list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(student_score[1:])/student_score[0]
    num = 0
    for score in student_score[1:] :
        if score > avg:
            num+=1
    rate = num/student_score[0]*100
    print(f'{rate:.3f}%')

# f 문자열 포매팅
# https://wikidocs.net/13
