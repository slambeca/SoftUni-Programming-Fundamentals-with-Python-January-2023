eff_employee_one = int(input())
eff_employee_two = int(input())
eff_employee_three = int(input())

students_count = int(input())

total_efficiency = eff_employee_one + eff_employee_two + eff_employee_three

hours = 0

while students_count > 0:
    if hours % 4 == 0:    # every 4th hour they take a brake
        hours += 1

    students_count -= total_efficiency

    if students_count <= 0:
        break

    hours += 1

print(f"Time needed: {hours}h.")

# Variant 2
# first_employee_people_count = int(input())
# second_employee_people_count = int(input())
# third_employee_people_count = int(input())
#
# people_count = int(input())
#
# people_per_hour = first_employee_people_count + second_employee_people_count + third_employee_people_count
#
# hours = 0
#
# while people_count > 0:
#     hours += 1
#
#     people_count -= people_per_hour
#
#     if hours % 4 == 0:
#         hours += 1
#
# print(f"Time needed: {hours}h.")