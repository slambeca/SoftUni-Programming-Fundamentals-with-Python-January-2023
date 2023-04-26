company_users = {}

while True:
    command = input()

    if command == "End":
        break

    company_name, employee = command.split(" -> ")

    if company_name not in company_users:
        company_users[company_name] = []

    if employee not in company_users[company_name]:
        company_users[company_name].append(employee)

for company in company_users.items():
    company_name = company[0]
    company_ids = company[1]
    print(company_name)

    for element in range(len(company_ids)):
        print(f"-- {company_ids[element]}")

# Variant 2 with different print
# dictionary = {}
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     company, identification = command.split(" -> ")
#
#     if company not in dictionary.keys():
#         dictionary[company] = []
#
#     if identification not in dictionary[company]:
#         dictionary[company].append(identification)
#
# for company, employees in dictionary.items():
#     print(company)
#
#     for employee in employees:
#         print(f"-- {employee}")