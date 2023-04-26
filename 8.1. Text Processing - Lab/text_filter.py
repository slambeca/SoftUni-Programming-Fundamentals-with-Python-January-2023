banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)

# Variant 2
# banned_words = input().split(", ")
# text = input()
#
# for word in banned_words:
#     text = text.replace(word, "*" * len(word))
#
# print(text)