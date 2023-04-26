def pass_check(password):
    """This function validates passwords."""
    pass_is_valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False

    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        pass_is_valid = False

    digit_counter = 0

    for character in password:
        if character.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False

    return pass_is_valid


input_password = input()

password_is_valid = (pass_check(input_password))

if password_is_valid:
    print("Password is valid")

# Variant 2 with a list, not a boolean
#
#
# def password_validator(password):
#     """This function validates passwords."""
#     is_password_valid = []
#
#     if len(password) < 6 or len(password) > 10:
#         is_password_valid.append("Password must be between 6 and 10 characters")
#
#     if not password.isalnum():
#         is_password_valid.append("Password must consist only of letters and digits")
#
#     counter = 0
#
#     for character in password:
#         if character.isdigit():
#             counter += 1
#
#     if counter < 2:
#         is_password_valid.append("Password must have at least 2 digits")
#
#     return is_password_valid    # the function returns a list
#
#
# input_password = input()
#
# password_validation = password_validator(input_password)    # this is a list
#
# if len(password_validation) == 0:
#     print("Password is valid")
# else:
#     print("\n".join(password_validation))
#
# # Variant 3 with three functions
#
#
# def is_valid_length(password):
#     return 6 <= len(password) <= 10
#
#
# def contains_alpha_numbers(password):
#     return password.isalnum()
#
#
# def contains_at_least_two_digits(password):
#     digits_counter = 0
#     for ch in password:
#         if ch.isdigit():
#             digits_counter += 1
#
#     return digits_counter >= 2
#
#
# input_password = input()
# is_valid = True
#
# if not is_valid_length(input_password):
#     is_valid = False
#     print("Password must be between 6 and 10 characters")
#
# if not contains_alpha_numbers(input_password):
#     is_valid = False
#     print("Password must consist only of letters and digits")
#
# if not contains_at_least_two_digits(input_password):
#     is_valid = False
#     print("Password must have at least 2 digits")
#
# if is_valid:
#     print("Password is valid")
