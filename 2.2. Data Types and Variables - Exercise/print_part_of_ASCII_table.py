start_index = int(input())
end_index = int(input())

for char in range(start_index, end_index + 1):
    print(chr(char), end=" ")    # we can remove the last space with strip() function

# Variant 2
# start = int(input())
# end = int(input())
#
# delimiter = " "
#
# result = ""
#
# for char in range(start, end + 1):
#     result += chr(char) + delimiter
#
# print(result)
