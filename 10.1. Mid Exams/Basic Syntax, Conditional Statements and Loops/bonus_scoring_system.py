from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_lectures_visited = 0

for _ in range(number_of_students):
    attendance = int(input())

    if attendance > max_lectures_visited:
        max_lectures_visited = attendance

    current_bonus = attendance / number_of_lectures * (5 + additional_bonus)    # possible ZeroDivisionError

    if current_bonus > max_bonus:
        max_bonus = current_bonus

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lectures_visited} lectures.")

# Variant 2
# from math import ceil
#
# students = int(input())
# lectures = int(input())
# bonus = int(input())
#
# max_attendances = 0
#
# for _ in range(students):
#     attendances = int(input())
#     max_attendances = max(attendances, max_attendances)
#
# total_bonus = 0
#
# if lectures != 0:
#     total_bonus = (max_attendances / lectures) * (5 + bonus)
#
# print(f"Max Bonus: {ceil(total_bonus)}.")
# print(f"The student has attended {max_attendances} lectures.")