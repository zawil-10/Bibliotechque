import unittest
from main import Utilisateur, Exemplaire, Ressource, Livre, Revue, Emplacement


class TestUtilisateur(unittest.TestCase):
    def test_emprunter_exemplaire(self):
        utilisateur = Utilisateur("zeze", "will", "will@gmail.com")
        exemplaire = Exemplaire(identifiant=1)
        utilisateur.emprunter(exemplaire)
        self.assertIn(exemplaire, utilisateur.emprunts)
        self.assertFalse(exemplaire.disponible)

    def test_retourner_exemplaire(self):
        utilisateur = Utilisateur("zeze", "will", "will@mail.com")
        exemplaire = Exemplaire(identifiant=1)
        utilisateur.emprunter(exemplaire)
        utilisateur.retourner(exemplaire)
        self.assertNotIn(exemplaire, utilisateur.emprunts)
        self.assertTrue(exemplaire.disponible)


class TestExemplaire(unittest.TestCase):
    def test_set_disponibilite(self):
        exemplaire = Exemplaire(identifiant=1)
        exemplaire.set_disponibilite(False)
        self.assertFalse(exemplaire.disponible)


class TestEmplacement(unittest.TestCase):
    def test_assigner_exemplaire(self):
        emplacement = Emplacement(rayon="A", etagere=1)
        exemplaire = Exemplaire(identifiant=1)
        emplacement.assigner_exemplaire(exemplaire)
        self.assertEqual(exemplaire.emplacement, emplacement)


class TestLivre(unittest.TestCase):
    def test_obtenir_ISBN(self):
        livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "1234567890")
        self.assertEqual(livre.obtenir_ISBN(), "1234567890")


class TestRevue(unittest.TestCase):
    def test_obtenir_numero(self):
        revue = Revue("Titre de la Revue", "Auteur de la Revue", 2023, 5)
        self.assertEqual(revue.obtenir_numero(), 5)


if __name__ == '__main__':
    unittest.main()
