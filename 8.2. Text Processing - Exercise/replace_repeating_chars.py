some_text = input()

final_text = ""
last_letter = ""

for letter in some_text:
    if letter != last_letter:
        final_text += letter
    last_letter = letter

print(final_text)

# Variant 2
# some_text = input()
#
# final_text = ""
# last_letter = ""
#
# for letter in some_text:
#     if letter != last_letter:
#         final_text += letter
#         last_letter = letter
#
# print(final_text)
#
# # Variant 3
# text = input()
# result = text[0]
#
# for ch in text:
#     if ch == result[-1]:
#         continue
#     result += ch
#
# print(result)