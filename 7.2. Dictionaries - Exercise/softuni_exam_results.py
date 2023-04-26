exam_results = {"submissions": {}, "results": {}}

while True:
    exam_info = input()

    if exam_info == "exam finished":
        break

    exam_info = exam_info.split("-")

    if len(exam_info) == 3:
        username = exam_info[0]
        language = exam_info[1]
        points = int(exam_info[2])

        if language not in exam_results["results"]:
            exam_results["results"][language] = {username: points}
            exam_results["submissions"][language] = 1

        elif language in exam_results["results"]:
            exam_results["submissions"][language] += 1
            if username in exam_results["results"][language]:
                if points > exam_results["results"][language][username]:
                    exam_results["results"][language][username] = points

            elif username not in exam_results["results"][language]:
                exam_results["results"][language][username] = points

    elif len(exam_info) < 3:
        username = exam_info[0]
        for language in exam_results["results"]:
            for name in exam_results["results"][language]:
                if name == username:
                    del exam_results["results"][language][name]
                    break

print("Results:")

for language in exam_results["results"]:
    for name in exam_results["results"][language]:
        print(f"{name} | {exam_results['results'][language][name]}")

print("Submissions:")

for language in exam_results["submissions"]:
    print(f"{language} - {exam_results['submissions'][language]}")

# Variant 2
# results = {}
# submissions = {}
#
# while True:
#     command = input()
#
#     if command == "exam finished":
#         break
#
#     command = command.split("-")
#
#     if len(command) == 3:
#         username = command[0]
#         language = command[1]
#         points = int(command[2])
#
#         if username not in results.keys():
#             results[username] = points
#         else:
#             if points > results[username]:
#                 results[username] = points
#
#         if language not in submissions.keys():
#             submissions[language] = 1
#         else:
#             submissions[language] += 1
#
#     elif len(command) < 3:
#         username = command[0]
#         del results[username]
#
# print("Results:")
# for key, value in results.items():
#     print(f"{key} | {value}")
# print("Submissions:")
# for key, value in submissions.items():
#     print(f"{key} - {value}")