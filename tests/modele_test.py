import unittest
from models import modele as modele

# Pour rouler les tests, utilisez la commande suivante dans le terminal :
# python -m unittest discover -v -s tests -p "*test.py"


class ModeleTest(unittest.TestCase):
    
    def test_exemple_de_fonction_test(self):
        self.assertEqual(modele.exemple_de_fonction_testee(2, 3), 5)
        self.assertEqual(modele.exemple_de_fonction_testee(1, 1), 2)