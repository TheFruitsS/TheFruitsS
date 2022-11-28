count = int(input())
students = {}
for _ in range(count):
    line = tuple(input().split())
    student, grade = line
    print(student , grade)
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
    print(f'{student} -> {grade} (avg: {sum(grade)})')

#for students in range(count):

