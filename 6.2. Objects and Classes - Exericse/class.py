class Class:
    __students_count = 22    # this is a class attribute, with __ at the front it is private for this class and can
    # not be accessed outside the class

    def __init__(self, name):
        self.name = name

        self.students = []    # those are default values
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):     # or Class.__students_count
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        avg_grade = sum(self.grades) / len(self.grades)
        return float(f"{avg_grade:.2f}")

    def __repr__(self):
        students = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"


a_class = Class("11B")

a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)

print(a_class)