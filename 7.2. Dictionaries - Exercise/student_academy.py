students_and_grades = {}

count_lines = int(input())

for student in range(count_lines):
    name = input()
    grade = float(input())

    if name not in students_and_grades.keys():
        students_and_grades[name] = []

    students_and_grades[name].append(grade)

for student, grades in students_and_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {sum(grades) / len(grades):.2f}")