messages = input().split()

for message in messages:
    whats_the_word = ""
    secret_message = ""

    letters = []

    letters_str = ""
    whole_message = ""

    for msg in range(len(message)):
        current_letter = message[msg]
        if current_letter.isdigit():
            whats_the_word += current_letter
        else:
            letters.append(current_letter)

    word = chr(int(whats_the_word))
    secret_message += word
    letters[0], letters[-1] = letters[-1], letters[0]

    for letter in letters:
        letters_str += letter

    whole_message = secret_message + letters_str

    print(whole_message, end=" ")