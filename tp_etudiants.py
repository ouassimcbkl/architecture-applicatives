from collections.abc import Iterable, Iterator

# --- Décorateurs pour Student et SchoolClass ---
def add_chemistry(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.chem_grade = 0
    cls.__init__ = new_init
    return cls

def add_matter_4_iterator(cls):
    def iter_matter_4(self):
        return ChemIterator(self.students)
    cls.iter_matter_4 = iter_matter_4
    return cls

# --- Classe Student ---
@add_chemistry
class Student:
    def __init__(self, name, math_grade, physics_grade, info_grade):
        self.name = name
        self.math_grade = math_grade
        self.physics_grade = physics_grade
        self.info_grade = info_grade

# --- Itérateurs ---
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

# --- Singleton + décorateur pour itérateur matière 4 ---
@add_matter_4_iterator
class SchoolClass(Iterable):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'students'):
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return MathIterator(self.students)

    def iter_matter_2(self):
        return PhysicsIterator(self.students)

    def iter_matter_3(self):
        return InfoIterator(self.students)


# --- Bloc main ---
# Peu importe où on crée l'instance, c'est la même
school_class1 = SchoolClass()
school_class2 = SchoolClass()

school_class1.add_student(Student('J', 10, 12, 13))
school_class2.add_student(Student('A', 8, 2, 17))
school_class1.add_student(Student('V', 9, 14, 14))

# Mise à jour chimie
school_class1.students[0].chem_grade = 15
school_class1.students[1].chem_grade = 12
school_class1.students[2].chem_grade = 18

# Vérification singleton : school_class1 et school_class2 contiennent les mêmes étudiants
print("Classement matière 4 (chimie) via singleton :")
for s in school_class2.iter_matter_4():
    print(s.name, ":", s.chem_grade)
