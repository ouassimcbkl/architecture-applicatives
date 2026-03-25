class Student:
    def __init__(self, name, math_grade, physics_grade, info_grade):
        self.name = name
        self.math_grade = math_grade
        self.physics_grade = physics_grade
        self.info_grade = info_grade


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# --- Code de test demandé par le professeur ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))
