while True:
    current_number = float(input())

    if 1 <= current_number <= 100:
        print(f"The number {current_number} is between 1 and 100")
        break

# Variant 2
# number = float(input())
#
# while number < 1 or number > 100:
#     number = float(input())
#
# print(f"The number {number} is between 1 and 100")
