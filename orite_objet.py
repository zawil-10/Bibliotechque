class Utilisateur(object):
    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.emprunts = []

    def emprunter(self, exemplaire):
        if exemplaire.disponible:
            exemplaire.disponible = False
            self.emprunts.append(exemplaire)
            print(f"{self.prenom} {self.nom} a emprunté l'exemplaire {exemplaire.identifiant}.")
        else:
            print("Cet exemplaire n'est pas disponible.")

    def retourner(self, exemplaire):
        if exemplaire in self.emprunts:
            exemplaire.disponible = True
            self.emprunts.remove(exemplaire)
            print(f"{self.prenom} {self.nom} a retourné l'exemplaire {exemplaire.identifiant}.")
        else:
            print("Cet exemplaire n'est pas emprunté par cet utilisateur.")


class Exemplaire:
    def __init__(self, identifiant, disponible=True):
        self.identifiant = identifiant
        self.disponible = disponible

    def set_disponibilite(self, disponible):
        self.disponible = disponible


class Ressource:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee


class Emplacement:
    def __init__(self, rayon, etagere):
        self.rayon = rayon
        self.etagere = etagere

    def assigner_exemplaire(self, exemplaire):
        exemplaire.emplacement = self


class Livre(Ressource):
    def __init__(self, titre, auteur, annee, isbn):
        super().__init__(titre, auteur, annee)
        self.isbn = isbn


class Revue(Ressource):
    def __init__(self, titre, auteur, annee, numero):
        super().__init__(titre, auteur, annee)
        self.numero = numero


# Création d'objets utilisant ces classes
utilisateur1 = Utilisateur("Doe", "John", "john@example.com")
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "1234567890")
exemplaire1 = Exemplaire(identifiant=1)
exemplaire2 = Exemplaire(identifiant=2)

# Attribution des exemplaires à des emplacements
emplacement1 = Emplacement(rayon="A", etagere=1)
emplacement2 = Emplacement(rayon="B", etagere=2)

# Utilisation des méthodes pour emprunter et retourner des exemplaires
utilisateur1.emprunter(exemplaire1)
utilisateur1.retourner(exemplaire1)
utilisateur1.emprunter(exemplaire2)
