students = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0


studentsgrades = 0

for _ in range(0, students):
    student = float(input())
    studentsgrades += student
    if student >= 5.00:
        count1 += 1
    if 4 <= student <= 4.99:
        count2 += 1
    if 3 <= student <= 3.99 and students :
        count3 += 1
    if student < 3:
        count4 += 1
group1 = count1 / students * 100
group2 = count2 / students * 100
group3 = count3 / students * 100
group4 = count4 / students * 100
studentsfinal = studentsgrades / students
print(f'Top students: {group1:.2f}%')
print(f'Between 4.00 and 4.99: {group2:.2f}%')
print(f'Between 3.00 and 3.99: {group3:.2f}%')
print(f'Fail: {group4:.2f}%')
print(f'Average: {studentsfinal:.2f}')
