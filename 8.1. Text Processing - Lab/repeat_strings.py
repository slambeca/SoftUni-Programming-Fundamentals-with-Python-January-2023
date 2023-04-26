text = input().split()

for word in text:
    print(word * len(word), end="")

# Variant 2 with list comprehension
# [print(s * len(s), end="") for s in input().split()]
#
# # Variant 3 with str concatenation
# words = input().split()
#
# result = ""
#
# for word in words:
#     result += word * len(word)
#
# print(result)