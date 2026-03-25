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

    def rank_matter_1(self):
        sorted_students = sorted(
            self.students,
            key=lambda student: student.math_grade,
            reverse=True
        )

        print("Classement matière 1 (maths) :")
        for student in sorted_students:
            print(student.name, ":", student.math_grade)

    # Nouvelle méthode demandée
    def rank_matter_2(self):
        sorted_students = sorted(
            self.students,
            key=lambda student: student.physics_grade,
            reverse=True
        )

        print("Classement matière 2 (physique) :")
        for student in sorted_students:
            print(student.name, ":", student.physics_grade)

    # Nouvelle méthode demandée
    def rank_matter_3(self):
        sorted_students = sorted(
            self.students,
            key=lambda student: student.info_grade,
            reverse=True
        )

        print("Classement matière 3 (informatique) :")
        for student in sorted_students:
            print(student.name, ":", student.info_grade)


# --- Bloc main ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()
