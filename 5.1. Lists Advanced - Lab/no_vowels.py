text = input()

vowels = ["a", "o", "e", "i", "u"]

result = []

for char in text:
    # make case-insensitive
    if char.lower() not in vowels:
        result.append(char)

print("".join(result))

# Variant 2
# vowels = ["a", "o", "e", "u", "i"]
#
# input_line = input()
#
# result = [x for x in input_line if x.lower() not in vowels]
#
# print("".join(result))
#
# # Variant 3
# new_vowels = ["a", "o", "e", "i", "u"]
#
#
# def remove_vowels(some_text):
#     new_result = [new_char for new_char in text if char.lower() not in vowels]
#     return "".join(new_result)
#
#
# input_text = input()
# print(remove_vowels(input_text))