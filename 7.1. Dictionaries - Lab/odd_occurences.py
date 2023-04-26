words = input().lower().split()    # ['java', 'c#', 'php', 'php', 'java', 'c', 'java']

dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = 0

    dictionary[word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")

# Variant 2
# words_keys = [el.lower() for el in input().split()]
# default = 0
#
# occurrences = dict.fromkeys(words_keys, default)
#
# for word in words_keys:
#     occurrences[word] += 1    # or words_keys.count(word)
#
# for word, count in occurrences.items():
#     if count % 2 != 0:
#         print(word, end=" ")