count_inputs = int(input())

for _ in range(count_inputs):
    current_input = int(input())
    if current_input == 88:
        print("Hello")
    elif current_input == 86:
        print("How are you?")
    elif current_input < 88:
        print("GREAT!")
    elif current_input > 88:
        print("Bye.")