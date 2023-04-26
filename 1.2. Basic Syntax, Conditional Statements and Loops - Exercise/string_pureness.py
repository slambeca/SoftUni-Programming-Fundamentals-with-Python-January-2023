count_strings = int(input())

for _ in range(count_strings):
    string = input()

    if "." in string or "," in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")

# Variant 2
# count_strings = int(input())
#
# for _ in range(count_strings):
#     string = input()
#
#     if "." not in string and "," not in string and "_" not in string:
#         print(f"{string} is pure.")
#     else:
#         print(f"{string} is not pure!")
#
# # Variant 3
# words_count = int(input())
#
# for _ in range(words_count):
#     word = input()
#
#     is_pure = True
#
#     for ch in word:
#         if ch == "," or ch == "." or ch == "_":
#             is_pure = False
#             break
#
#     if is_pure:
#         print(f"{word} is pure.")
#     else:
#         print(f"{word} is not pure!")