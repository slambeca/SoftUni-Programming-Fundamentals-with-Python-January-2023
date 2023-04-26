from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())

number_of_courses = number_of_people / elevator_capacity

print(ceil(number_of_courses))