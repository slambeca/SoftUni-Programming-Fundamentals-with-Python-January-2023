input_line = input().split(".")

file_path = input_line[0]    # C:\Projects\Data-Structures\LinkedList -> the name is always the last element,
# so we should use index [-1]
extension = input_line[1]

path_elements = file_path.split("\\")

print(f"File name: {path_elements[-1]}")
print(f"File extension: {extension}")

# Variant 2
# file_name = input().split("\\")[-1]
#
# print(f"File name: {file_name.split('.')[0]}\nFile extension: {file_name.split('.')[1]}")
#
# # Variant 3 with RegEx
# import re
#
# filename_with_extension = input()
#
# filename, extension = re.search("(\w+)\.(\w+)$", filename_with_extension).groups()
#
# print(f"File name: {filename}")
# print(f"File extension: {extension}")
#
# # 60/100 in Judge
#
# # Variant 4
# file = input().split("\\")[-1].split(".")
#
# print(f"File name: {file[0]}\nFile extension: {file[1]}")