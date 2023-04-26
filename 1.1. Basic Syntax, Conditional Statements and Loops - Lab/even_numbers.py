number = int(input())

is_odd = False

for _ in range(1, number + 1):
    current_number = int(input())

    if current_number % 2 == 0:
        continue
    else:
        print(f"{current_number} is odd!")
        is_odd = True
        break

if not is_odd:
    print("All numbers are even.")

# Variant 2
# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#     if not number % 2 == 0:
#         print(f"f{number} is odd!")
#     else:
#         print("All numbers are even.")
#
# # Variant 3
# n = int(input())
#
# all_nums_are_even = True
#
# for _ in range(n):
#     number = int(input())
#
#     if number % 2 != 0:
#         all_nums_are_even = False
#         print(f"{number} is odd!")
#         break
#
# if all_nums_are_even:
#     print("All numbers are even.")
#
# # Variant 4
# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#
#     if number % 2 != 0:
#         print(f"{number} is odd!")
#         break
#
# else:
#     print("All numbers are even.")
#
# # Variant 5 - not recommended to use exit() here
# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#
#     if number % 2 != 0:
#         print(f"{number} is odd!")
#         exit()
#
# else:
#     print("All numbers are even.")
