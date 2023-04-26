number_of_snowballs = int(input())    # made by both of them

snowball_value = 0    # or float("-inf'") or -sys.maxsize

highest_snowball_value = 0
weight_highest_value = 0
time_needed_highest_value = 0
quality_highest_value = 0

for _ in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight / time_needed) ** quality

    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        weight_highest_value = weight
        time_needed_highest_value = time_needed
        quality_highest_value = quality

print(f"{weight_highest_value} : {time_needed_highest_value} = {highest_snowball_value:.0f} ({quality_highest_value})")

# Variant 2
# n = int(input())
#
# best_snowball = float("-inf")
#
# output = ""
#
# for idx in range(n):
#     weight = int(input())
#     time = int(input())
#     quality = int(input())
#
#     result = (weight // time) ** quality
#
#     if result > best_snowball:
#         best_snowball = result
#         output = f"{weight} : {time} = {result} ({quality})"
#
# print(output)