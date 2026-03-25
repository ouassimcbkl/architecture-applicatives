from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name, math_grade, physics_grade, info_grade):
        self.name = name
        self.math_grade = math_grade
        self.physics_grade = physics_grade
        self.info_grade = info_grade


class StudentIterator(Iterator):
    def __init__(self, students):
        # trier décroissant sur la matière 1 (math_grade)
        self.sorted_students = sorted(students, key=lambda s: s.math_grade, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students)


# --- Bloc main ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

# Utilisation de l'itérateur
print("Classement matière 1 via itérateur :")
for student in school_class:
    print(student.name, ":", student.math_grade)
