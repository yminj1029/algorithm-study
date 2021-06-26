# 3. 성적이 낮은 순서로 학생 출력하기

n = int(input())  # 학생 수.
students = []
for i in range(n):
    student = input().split()
    students.append((student[0], int(student[1])))

# 성적이 낮은 순서대로 학생의 이름을 출력한다.
# 파이썬 정렬 라이브러리 사용

students = sorted(students, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in students:
    print(student[0], end=' ')
