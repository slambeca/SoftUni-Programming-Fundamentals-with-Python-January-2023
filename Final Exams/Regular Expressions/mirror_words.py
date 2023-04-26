import re

data = input() # @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@
# ##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r

pattern = r"(\@|\#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"

result = re.findall(pattern, data)
# [('#', 'poOl', '##', 'loOp', '#'), ('#', 'Part', '##', 'traP', '#'), ('@', 'leveL', '@@', 'Level', '@'),
# ('@', 'pack', '@@', 'ckap', '@'), ('#', 'sAw', '##', 'wAs', '#')]

mirrors_words = []

counter = 0

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirrors_words.append(f"{pair[1]} <=> {pair[3]}")
    counter += 1    # or we use len(result) at the end

if counter > 0:
    print(f"{counter} word pairs found!")
    if not mirrors_words:
        print(f"No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirrors_words))
else:
    print(f"No word pairs found!")
    print(f"No mirror words!")

# # Variant 2
# import re
#
# data = input()
#
# pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)'
# hidden_words = re.findall(pattern, data)
# mirror_words = []
#
# for word in hidden_words:
#     if word[1] == word[3][::-1]:
#         mirror_words.append([word[1], word[3]])
#
# result = ''
#
# if hidden_words:
#     print(f'{len(hidden_words)} word pairs found!')
# else:
#     print('No word pairs found!')
#
# if mirror_words:
#     print('The mirror words are:')
#     for pair in mirror_words:
#         result += pair[0] + ' <=> ' + pair[1] + ', '
#     print(result[0:-1 - 1])
# else:
#     print('No mirror words!')
#
# # Variant 3
# import re
#
# text_input = input()
#
# words_found = 0
# mirror_words = {}
#
# pattern = r"(@|#)([A-z]{3,})\1((@|#)([A-z]{3,})\1)"
#
# matches = re.findall(pattern, text_input)
# #print(matches)
#
# for match in matches:
#     words_found += 1
#
#     rev_group_2 = match[4]
#     rev_group_2 = rev_group_2[::-1]
#
#     if match[1] == rev_group_2:
#         word = match[1]
#         mirr_word = match[4]
#         mirror_words[word] = mirr_word
#
# if words_found >= 1:
#     print(f"{words_found} word pairs found!")
# else:
#     print(f"No word pairs found!")
#
# if not mirror_words:
#     print(f"No mirror words!")
# else:
#     print(f'The mirror words are:')
#     print(', '.join('{} <=> {}'.format(k, v) for k,v in mirror_words.items()))