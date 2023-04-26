numbers = input().split()
message = input()

new_word = []

for sequence in numbers:  # [9992, 562, 8933]
    current_sum = 0  # 29
    for index in sequence:  # [9, 9, 9, 2]
        current_sum += int(index)  # 0 + 9 + 9 + 9 + 2

    current_sum = current_sum % len(message)
    new_word.append(message[current_sum])
    message = message.replace(message[current_sum], "", 1)

for i in new_word:
    print(i, end="")

# Variant 2
# numbers = input().split()
# text = list(input())
# new_string = ""
#
# for i in range(len(numbers)):
#     digits_sum = 0
#
#     for number in numbers[i]:
#         digit = int(number)
#         digits_sum += digit
#
#     if digits_sum > len(text) - 1:
#         new_index = digits_sum % len(text)
#         new_string += text[new_index]
#         text.pop(new_index)
#
#     else:
#         new_string += text[digits_sum]
#         text.pop(digits_sum)
#
# print(new_string)