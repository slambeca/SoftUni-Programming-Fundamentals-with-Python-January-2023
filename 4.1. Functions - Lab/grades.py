def grade_receiver(current_grade):
    """This function calculates grades."""
    if 2.00 <= current_grade <= 2.99:
        print("Fail")
    elif 3.00 <= current_grade <= 3.49:
        print("Poor")
    elif 3.50 <= current_grade <= 4.49:
        print("Good")
    elif 4.50 <= current_grade <= 5.49:
        print("Very Good")
    elif 5.50 <= current_grade <= 6.00:
        print("Excellent")


user_grade = float(input())

grade_receiver(user_grade)

# Variant 2
#
#
# def type_of_grade(score):
#     """This function calculates grades."""
#     if 2.00 <= score <= 2.99:
#         return "Fail"
#     elif 3.00 <= score <= 3.49:
#         return "Poor"
#     elif 3.50 <= score <= 4.49:
#         return "Good"
#     elif 4.50 <= score <= 5.49:
#         return "Very Good"
#     elif 5.50 <= score <= 6.00:
#         return "Excellent"
#
#
# grade = float(input())
# print(type_of_grade(grade))
#
# # Variant 3
#
#
# def grade_receiver(new_grade):
#     """This function calculates grades."""
#     result = None
#
#     if 2.00 <= new_grade <= 2.99:
#         result = "Fail"
#     elif 3.00 <= new_grade <= 3.49:
#         result = "Poor"
#     elif 3.50 <= new_grade <= 4.49:
#         result = "Good"
#     elif 4.50 <= new_grade <= 5.49:
#         result = "Very Good"
#     elif 5.50 <= new_grade <= 6.00:
#         result = "Excellent"
#
#     return result
#
#
# user_grade = float(input())
#
# print(grade_receiver(user_grade))