def characters_between(num1, num2):
    """This function prints the characters from the ASCII table between a given range."""
    for i in range(ord(num1) + 1, ord(num2)):
        print(chr(i), end=" ")    # this way we will have a blank space at the end of our output


string_one = input()
string_two = input()

characters_between(string_one, string_two)

# Variant 2 with list unpacking  and join(), not string (this way we won`t have a blank space at the end of our output)
#
#
# def collect_characters(first, second):
#     """This function prints the characters from the ASCII table between a given range."""
#     characters = []
#     for i in range(ord(first) + 1, ord(second)):
#         characters.append(chr(i))
#
#     return " ".join(characters)    # this way we are limiting the functionality of this f(),
#     # join() should be in the print() at the end
#
#
# first_character = input()
# second_character = input()
#
# result = collect_characters(first_character, second_character)
# print(result)
# # or print(*result)              -> default sep is " " in this case
# # or print(*result, sep= " ")