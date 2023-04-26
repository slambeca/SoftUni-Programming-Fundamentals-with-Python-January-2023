def check_data_type(data_type, num):
    if data_type == "int":
        return int(num) * 2
    elif data_type == "real":
        return f"{(float(num) * 1.5):.2f}"
    elif data_type == "string":
        return f"${num}$"


command = input()
number = input()

print(check_data_type(command, number))