from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name, math_grade, physics_grade, info_grade):
        self.name = name
        self.math_grade = math_grade
        self.physics_grade = physics_grade
        self.info_grade = info_grade


# Itérateur matière 1 (math)
class MathIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.math_grade, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

# Itérateur matière 2 (physique)
class PhysicsIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.physics_grade, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

# Itérateur matière 3 (info)
class InfoIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.info_grade, reverse=True)
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

    # itérable par défaut → matière 1
    def __iter__(self):
        return MathIterator(self.students)

    def iter_matter_2(self):
        return PhysicsIterator(self.students)

    def iter_matter_3(self):
        return InfoIterator(self.students)


# --- Bloc main ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

print("Classement matière 1 (math) :")
for student in school_class:
    print(student.name, ":", student.math_grade)

print("\nClassement matière 2 (physique) :")
for student in school_class.iter_matter_2():
    print(student.name, ":", student.physics_grade)

print("\nClassement matière 3 (info) :")
for student in school_class.iter_matter_3():
    print(student.name, ":", student.info_grade)
