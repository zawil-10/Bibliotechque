class Utilisateur:
    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email

class Exemplaire:
    def __init__(self, identifiant, disponible=True):
        self.identifiant = identifiant
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
exemplaire1 = Exemplaire(identifiant="1")
exemplaire2 = Exemplaire(identifiant="2")

# Attribution des exemplaires à des emplacements
emplacement1 = Emplacement(rayon="A", etagere="1")
emplacement2 = Emplacement(rayon="B", etagere="2")

# Simulation d'emprunt et de retour
def emprunter_exemplaire(utilisateur, exemplaire):
    if exemplaire.disponible:
        exemplaire.disponible = False
        print(f"L'exemplaire {exemplaire.identifiant} a été emprunté par {utilisateur.nom} {utilisateur.prenom}.")
    else:
        print("Cet exemplaire n'est pas disponible.")

def retourner_exemplaire(exemplaire):
    exemplaire.disponible = True
    print(f"L'exemplaire {exemplaire.identifiant} a été retourné.")

# Utilisation des fonctions pour emprunter et retourner des exemplaires
emprunter_exemplaire(utilisateur1, exemplaire1)
retourner_exemplaire(exemplaire1)
emprunter_exemplaire(utilisateur1, exemplaire2)
