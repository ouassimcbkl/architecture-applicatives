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

    # Méthode demandée par le professeur
    def rank_matter_1(self):
        sorted_students = sorted(
            self.students,
            key=lambda student: student.math_grade,
            reverse=True
        )

        print("Classement matière 1 (maths) :")
        for student in sorted_students:
            print(student.name, ":", student.math_grade)


# --- Bloc main / code de test ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

# appel de la méthode demandé
school_class.rank_matter_1()
