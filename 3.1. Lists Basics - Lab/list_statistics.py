n = int(input())

list_positives = []
list_negatives = []

count_positives = 0
sum_of_negatives = 0

for _ in range(n):
    current_number = int(input())

    if current_number > 0:
        list_positives.append(current_number)
        count_positives += 1
    elif current_number < 0:
        list_negatives.append(current_number)
        sum_of_negatives += current_number

print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}\nSum of negatives: {sum_of_negatives}")

# Variant 2
# n = int(input())
#
# list_positives = []
# list_negatives = []
#
# for _ in range(n):
#     current_number = int(input())
#
#     if current_number > 0:    # or >= 0
#         list_positives.append(current_number)
#     elif current_number < 0:    # or else
#         list_negatives.append(current_number)
#
# print(list_positives)
# print(list_negatives)
# print(f"Count of positives: {len(list_positives)}\nSum of negatives: {sum(list_negatives)}")