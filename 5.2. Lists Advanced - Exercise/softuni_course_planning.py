def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)    # insert the lesson at the end of the lessons list

    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)    # insert the lesson at the given index

    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):    # we check if the index is a positive
            if "Exercise" in list_of_lessons[title_index + 1]:    # if Exercise in sitting in the next index
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)

    return list_of_lessons


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
        list_of_lessons[first_position], list_of_lessons[second_position] = \
            list_of_lessons[second_position], list_of_lessons[first_position]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, f"{title}-Exercise")
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")

while len(command) > 1:    # len(command) of "course start" = 1
    action = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        lesson_title_or_index = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)    # we will modify the initial list with the function
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(lesson_title_or_index))
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, lesson_title_or_index)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input().split(":")

for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")

# Variant 2 with no functions
# initial_schedule = input().split(", ")  # ["Data Types", "Objects", "Lists"]
#
# while True:
#     command = input()
#
#     if command == "course start":
#         break
#
#     command_args = command.split(":")  # ["Add", "Databases"]
#
#     type_of_command = command_args[0]  # "Add"
#     lesson = command_args[1]  # Databases
#
#     if type_of_command == "Add":
#         if lesson not in initial_schedule:
#             initial_schedule.append(lesson)
#
#     elif type_of_command == "Insert":
#         lesson_index = int(command_args[2])
#         if lesson not in initial_schedule:
#             initial_schedule.insert(lesson_index, lesson)
#
#     elif type_of_command == "Remove":
#         if lesson in initial_schedule:
#             current_lesson_index = initial_schedule.index(lesson)  # the index is 3
#             if current_lesson_index + 1 in range(len(initial_schedule)):
#                 if "Exercise" in initial_schedule[current_lesson_index + 1]:
#                     initial_schedule.pop(current_lesson_index + 1)
#             initial_schedule.remove(lesson)
#
#     elif type_of_command == "Swap":
#         second_lesson = command_args[2]
#         if lesson in initial_schedule and second_lesson in initial_schedule:
#             first_position = initial_schedule.index(lesson)
#             second_position = initial_schedule.index(second_lesson)
#             first_has_exercise = False
#             second_has_exercise = False
#             if first_position + 1 in range(len(initial_schedule)):
#                 first_has_exercise = "Exercise" in initial_schedule[first_position + 1]
#             if second_position + 1 in range(len(initial_schedule)):
#                 second_has_exercise = "Exercise" in initial_schedule[second_position + 1]
#             initial_schedule[first_position], initial_schedule[second_position] = \
#                 initial_schedule[second_position], initial_schedule[first_position]
#             if first_has_exercise and second_has_exercise:
#                 initial_schedule[first_position + 1], initial_schedule[second_position + 1] = \
#                     initial_schedule[second_position + 1], initial_schedule[first_position + 1]
#             elif not first_has_exercise and second_has_exercise:
#                 initial_schedule.insert(first_position + 1, initial_schedule.pop(second_position + 1))
#             elif first_has_exercise and not second_has_exercise:
#                 initial_schedule.insert(second_position + 1, initial_schedule.pop(first_position + 1))
#
#     elif type_of_command == "Exercise":
#         if lesson in initial_schedule and f"{lesson}-Exercise" not in initial_schedule:
#             current_lesson_index = initial_schedule.index(lesson)
#             initial_schedule.insert(current_lesson_index + 1, f"{lesson}-Exercise")
#         elif lesson not in initial_schedule:
#             initial_schedule.append(lesson)
#             initial_schedule.append(f"{lesson}-Exercise")
#
# for idx, lesson in enumerate(initial_schedule):
#     print(f"{idx + 1}.{lesson}")