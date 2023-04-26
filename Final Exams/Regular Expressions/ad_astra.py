# Extract the information about the food and calculate the total calories
import re

data = input()

pattern = r"(\||#)([A-Za-z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d{1,5})(\1)"

result = re.findall(pattern, data)
# [('#', 'Bread', '#', '19/03/21', '#', '4000', '#'), ('|', 'Apples', '|', '08/10/20', '|', '200', '|'),
# ('|', 'Carrots', '|', '06/08/20', '|', '500', '|')]

total_calories = 0  # 4700
total_days = 0

for item in result:
    total_calories += int(item[5])

total_days = total_calories // 2000

print(f"You have food to last you for: {total_days} days!")

if result:
    for item in result:
        print(f"Item: {item[1]}, Best before: {item[3]}, Nutrition: {item[5]}")

# # Variant 2
# import re
#
# txt = input()
#
# pattern = r"(?P<symb>[\|#])(?P<name>[a-zA-z ]{1,})(?P=symb)" \
#           r"(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})(?P=symb)" \
#           r"(?P<cal>[0-9]{1,5})(?P=symb)"
#
# all_food = re.finditer(pattern, txt)
# cal_sum = sum([int(val.groupdict()["cal"]) for val in all_food])
# days = cal_sum // 2000
#
# print(f"You have food to last you for: {days} days!")
#
# result = re.findall(pattern, txt)
#
# for val in result:
#     print(f"Item: {val[1]}, Best before: {val[2]}, Nutrition: {val[3]}")
#
# # Variant 3
# import re
#
# text = input()
#
# pattern = r"(\||#)([A-Za-z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d{1,5})(\1)"
#
# results = re.findall(pattern, text)
#
# total_calories = 0
# products = []
#
# for result in results:
#     product = result[1]
#     expiration_date = result[3]
#     calories = int(result[5])
#
#     products.append(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")
#     total_calories += calories
#
# days = total_calories // 2000
# print(f"You have food to last you for: {days} days!")
# print("\n".join(products))