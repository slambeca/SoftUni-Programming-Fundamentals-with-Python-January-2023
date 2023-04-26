def loading_bar(number):
    for symbol in range(1, number + 1, 10):
        symbol = int(number / 10) * "%"; dot = int((100 - number) / 10) * "."
        if dot:
            result = f"{number}% [{symbol}{dot}]\nStill loading..."
        else:
            result = f"{number}% Complete!\n[{symbol}{dot}]"
    return result


integer = int(input())
print(loading_bar(integer))

# Variant 2
#
#
# def loading_bar(number):
#     for symbol in range(1, number + 1, 10):
#         symbol = int(number / 10) * "%"; dot = int((100 - number) / 10) * "."
#         result = f"{number}% [{symbol}{dot}]\nStill loading..."
#         if not dot:
#             result = f"{number}% Complete!\n[{symbol}{dot}]"
#     return result
#
#
# integer = int(input())
# print(loading_bar(integer))
#
# # Variant 3 with 8 lines of code with gypsy techniques
#
#
# def loading_bar(number):
#     for symbol in range(1, number + 1, 10):
#         symbol = int(number / 10) * "%"; dot = int((100 - number) / 10) * "."
#     if not dot:
#         print(f"{number}% Complete!\n[{symbol}{dot}]")
#     else:
#         print(f"{number}% [{symbol}{dot}]\nStill loading...")
#
#
# loading_bar(int(input()))
#
# # Variant 4 - shortest variant on 8 lines without for loop
#
#
# def status(number):
#     if number == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#     return f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."
#
#
# input_number = int(input())
# print(status(input_number))