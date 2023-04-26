def list_manipulator(numbers: list, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            numbers = list(args[2:]) + numbers

        elif args[1] == "end":
            numbers = numbers + list(args[2:])

    elif args[0] == "remove":
        if args[1] == "beginning":
            if len(args) == 3:
                for i in range(args[2]):
                    if numbers:
                        numbers = numbers[1:]
            else:
                numbers = numbers[1:]

        elif args[1] == "end":
            if len(args) == 3:
                for i in range(args[2]):
                    if numbers:
                        numbers = numbers[:-1]
            else:
                numbers = numbers[:-1]

    return numbers