numbers = input().split(", ")

positives = [num for num in numbers if int(num) >= 0]    # so that our list consists of strings, not ints
negatives = [num for num in numbers if int(num) < 0]
even = [num for num in numbers if int(num) % 2 == 0]
odd = [num for num in numbers if int(num) % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

# Variant 2 with 75% less iterations
# numbers = [int(x) for x in input().split(", ")]
#
# positives = []
# negatives = []
# evens = []
# odds = []
#
# for num in numbers:
#     if num >= 0:
#         positives.append(str(num))
#     else:
#         negatives.append(str(num))
#
#     if num % 2 == 0:
#         evens.append(str(num))
#     else:
#         odds.append(str(num))
#
# print(f"Positive: {', '.join(positives)}")
# print(f"Negative: {', '.join(negatives)}")
# print(f"Even: {', '.join(evens)}")
# print(f"Odd: {', '.join(odds)}")