input_string = input()
input_counter = int(input())


def my_func(string, counter):
    """This function repeats a given string, using a repeat value."""
    result = input_string * counter
    return result


print(my_func(input_string, input_counter))

# Variant 2 with lambda
# input_string = input()
# input_counter = int(input())
#
# repeated_string = lambda a, b: a * b
#
#
# print(repeated_string(input_string, input_counter))