class Etudiant:
    def __init__(self, nom, note_maths, note_physique, note_info):
        self.nom = nom
        self.note_maths = note_maths
        self.note_physique = note_physique
        self.note_info = note_info


class Classe:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
