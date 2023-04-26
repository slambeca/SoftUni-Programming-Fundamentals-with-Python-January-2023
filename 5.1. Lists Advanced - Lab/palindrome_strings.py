words = input().split()    # ['wow', 'father', 'mom', 'wow', 'shirt', 'stats']
palindrome = input()    # wow

list_with_palindromes = []    # ['wow', 'mom', 'wow', 'stats']

for word in words:
    if word == word[::-1]:
        list_with_palindromes.append(word)

count_palindromes = list_with_palindromes.count(palindrome)

print(list_with_palindromes)
print(f"Found palindrome {count_palindromes} times")