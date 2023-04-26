user_input = input()

while user_input != "End":
    command = user_input

    if command == "SoftUni":
        pass
    else:
        repeated_string = "".join([ch * 2 for ch in command])
        print(repeated_string)

    user_input = input()

# # Variant 2
# while True:
#     line = input()
#
#     if line == "End":
#         break
#
#     if line == "SoftUni":
#         continue
#
#     for ch in line:
#         print(f"{ch}{ch}", end="")
#
#     print()
#
# # Variant 3
# converted_line = ""
#
# for ch in line:
#     converted_line += 2 * ch
