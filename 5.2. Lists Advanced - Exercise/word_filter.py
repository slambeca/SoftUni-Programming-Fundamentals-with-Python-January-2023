# This variant is not recommended
print("\n".join([word for word in input().split() if len(word) % 2 == 0]))

# This is the recommended list comprehension depth
# words = input().split()
#
# filtered_words = [word for word in words if len(word) % 2 == 0]
#
# print("\n".join(filtered_words))
#
# # Variant 3
# words = input().split()
#
# result = list(filter(lambda x: len(x) % 2 == 0, words))
#
# print("\n".join(result))