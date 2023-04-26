students = {}

command = input().split(":")    # ['Peter', '123', 'programming basics']

while len(command) > 1:
    name, id, course = command[0], command[1], command[2]

    if course not in students.keys():    # if course not in students:
        students[course] = []    # we are adding empty lists in the dictionary

    students[course].append(f"{name} - {id}")    # we are appending each student to the corresponding course

    command = input().split(":")

searched_course = command[0].replace("_", " ")    # programming_basics -> programming basics

for student in students[searched_course]:
    print(student)
    
# print("\n".join(students[searched_course]

# Variant 2
# data = input()
#
# courses = {}
#
# while ":" in data:
#     student_name, student_id, course_name = data.split(":")
#     if course_name not in courses.keys():
#         courses[course_name] = {student_id: student_name}
#     else:
#         courses[course_name][student_id] = student_name
#
#     data = input()
#
# course_name = " ".join(data.split("_"))
# students = courses[course_name]
#
# for student_id, name in students.items():
#     print(f"{name} - {student_id}")