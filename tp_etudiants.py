from collections.abc import Iterable, Iterator

# --- Décorateur de classe ---
def add_chemistry(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.chem_grade = 0  # note par défaut pour la nouvelle matière

    cls.__init__ = new_init
    return cls

# --- Classe Student décorée ---
@add_chemistry
class Student:
    def __init__(self, name, math_grade, physics_grade, info_grade):
        self.name = name
        self.math_grade = math_grade
        self.physics_grade = physics_grade
        self.info_grade = info_grade


# --- Itérateurs existants ---
class MathIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.math_grade, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.sorted_students):
            s = self.sorted_students[self.index]
            self.index += 1
            return s
        else:
            raise StopIteration

class PhysicsIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.physics_grade, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.sorted_students):
            s = self.sorted_students[self.index]
            self.index += 1
            return s
        else:
            raise StopIteration

class InfoIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.info_grade, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.sorted_students):
            s = self.sorted_students[self.index]
            self.index += 1
            return s
        else:
            raise StopIteration

# --- Nouvel itérateur pour la 4ème matière ---
class ChemIterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.chem_grade, reverse=True)
        self.index = 0
    def __next__(self):
        if self.index < len(self.sorted_students):
            s = self.sorted_students[self.index]
            self.index += 1
            return s
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

    def iter_matter_4(self):
        return ChemIterator(self.students)


# --- Bloc main ---
school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

# Mise à jour des notes de chimie
school_class.students[0].chem_grade = 15
school_class.students[1].chem_grade = 12
school_class.students[2].chem_grade = 18

print("Classement matière 1 (math) :")
for s in school_class:
    print(s.name, ":", s.math_grade)

print("\nClassement matière 2 (physique) :")
for s in school_class.iter_matter_2():
    print(s.name, ":", s.physics_grade)

print("\nClassement matière 3 (info) :")
for s in school_class.iter_matter_3():
    print(s.name, ":", s.info_grade)

print("\nClassement matière 4 (chimie) :")
for s in school_class.iter_matter_4():
    print(s.name, ":", s.chem_grade)
