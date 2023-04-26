def check_for_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def check_for_al_num(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def check_for_spaces(name):
    if " " not in name:
        return True
    return False


def final_validation(name):
    if check_for_length(name) and check_for_al_num(name) and check_for_spaces(name):
        return True
    return False


usernames = input().split(", ")    # ['sh', 'too_long_username', '!lleg@l ch@rs', 'jeffbutt']

for username in usernames:
    if final_validation(username):
        print(username)

# Variant 2
#
#
# def check_for_char(some_word):
#     for char in some_word:
#         if not (char.isalnum() or char == "-" or char == "_"):
#             return False
#     return True
#
#
# words = input().split(", ")
#
# for word in words:
#     if 3 <= len(word) <= 16:
#         if check_for_char(word):
#             if " " not in word:
#                 print(word)
#
# # Variant 3
# from string import ascii_letters, digits
#
# usernames = input().split(", ")
#
# allowed_chars = ascii_letters + digits + "-" + "_"
#
# for username in usernames:
#     if len(username) < 3 or len(username) > 16:
#         continue
#
#     contains_allowed_char = all([char in allowed_chars for char in username])
#
#     if not contains_allowed_char:
#         continue
#
#     print(username)