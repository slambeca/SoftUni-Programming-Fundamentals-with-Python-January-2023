# Check if the given sequence of characters is a valid barcode or not
import re

count_barcodes = int(input())

# Should be surrounded by a "@" followed by one or more "#"
# It is at least 6 characters long (without the surrounding symbols)
# It starts with a capital letter
# It contains only letters (lower and uppercase) and digits
# It ends with a capital letter
pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)"
# pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"    # The barcode should be the only thing on the line!

for _ in range(count_barcodes):
    barcode = input()    # @#FreshFisH@#

    result = re.match(pattern, barcode)

    if not result:
        print("Invalid barcode")
    else:
        extract_nums = re.findall("\d", result.group())    # check if there are digits in the string
        # We use group when we have a match object

        if not extract_nums:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")    # concatenating the digits in the string

# # Variant 2
# import re
#
# count_lines = int(input())
#
# pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"    # The barcode should be the only thing on the line!
#
# for _ in range(count_lines):
#     text = input()
#
#     if re.match(pattern, text):
#         digits = re.findall("\d", text)
#
#         if digits:
#             product_group = ''.join(digits)
#         else:
#             product_group = "00"
#
#         print(f"Product group: {product_group}")
#     else:
#         print(f"Invalid barcode")
#
# # Variant 3
#
# import re
#
# count_of_barcodes = int(input())
#
# for value in range(count_of_barcodes):
#     barcode = input()
#     barcode_pattern = r'\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'
#     is_valid = re.findall(barcode_pattern, barcode)
#
#     if is_valid:
#         barcode = ''.join(is_valid)
#         product_group = ''.join([x for x in barcode if x.isdigit()])
#         if not product_group:
#             product_group = '00'
#         print(f'Product group: {product_group}')
#     else:
#         print('Invalid barcode')
#
# # Variant 4
# import re
#
# pattern = r"(?P<first_symbol>@#{1,})(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<last_symbol>@#{1,})"
#
# barcodes_count = int(input())
#
# for _ in range(barcodes_count):
#     barcode = input()
#     digits = ""
#     is_valid = re.match(pattern, barcode)
#     if is_valid:
#         valid_barcode = is_valid.groupdict()
#         for ch in valid_barcode["barcode"]:
#             if ch.isdigit():
#                 digits += ch
#         if len(digits) == 0:
#             print(f"Product group: 00")
#         else:
#             print(f"Product group: {digits}")
#     else:
#         print("Invalid barcode")
#
# # Variant 5
# import re
# n = int(input())
#
# for i in range(n):
#     text = input()
#     pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
#     match = re.match(pattern, text)
#
#     if match is None:
#         print("Invalid barcode")
#         continue
#
#     valid_barcode = match.group(1)
#     digits = ""
#
#     for ch in valid_barcode:
#         if ch.isdigit():
#             digits += ch
#
#     if digits == "":
#         print(f'Product group: 00')
#     else:
#         print(f'Product group: {digits}')
#
# # Variant 6 with re.compile()
# import re
#
# pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
#
# regex = re.compile(pattern)
# digit_regex = re.compile(r"\d")
#
# count_lines = int(input())
#
# for _ in range(count_lines):
#     row_data = input()
#
#     if regex.match(row_data):
#         digits = digit_regex.findall(row_data)
#         if digits:
#             product_group = "".join(digits)
#         else:
#             product_group = "00"
#
#         print(f"Product group: {product_group}")
#
#     else:
#         print("Invalid barcode")