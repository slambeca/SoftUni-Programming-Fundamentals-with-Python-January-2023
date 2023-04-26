courses = {}

while True:
    command = input()

    if command == "end":
        break

    course, student = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course in courses.items():
    current_course = course[0]
    students = course[1]
    print(f"{current_course}: {len(students)}")

    for student in range(len(students)):
        print(f"-- {students[student]}")

# Variant 2
#
#
# def check_for_item(some_item, some_array):
#     if some_item not in some_array:
#         return True
#     return False
#
#
# dictionary = {}
#
# while True:
#     command = input()
#
#     if command == "end":
#         break
#
#     course, student = command.split(" : ")
#
#     if check_for_item(course, dictionary):
#         dictionary[course] = []
#     dictionary[course].append(student)
#
# for course in dictionary.items():
#     current_course = course[0]
#     students = course[1]
#     print(f"{current_course}: {len(students)}")
#
#     for student in range(len(students)):
#         print(f"-- {students[student]}")
#
# # Variant 3 with print variation
#
#
# def check_for_item(some_item, some_array):
#     if some_item not in some_array:
#         return True
#     return False
#
#
# dictionary = {}
#
# while True:
#     command = input()
#
#     if command == "end":
#         break
#
#     course, student = command.split(" : ")
#
#     if check_for_item(course, dictionary):
#         dictionary[course] = []
#     dictionary[course].append(student)
#
# for course, students in dictionary.items():
#     print(f"{course}: {len(students)}")
#
#     for student in students:
#         print(f"-- {student}")