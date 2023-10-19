import unittest
from model.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def setUp(self):
        self.antibiotico = Antibiotico("A12345", 500, "Bovinos", "Amoxicilina", 100.0)

    def test_inicializacion_antibiotico(self):
        self.assertEqual(self.antibiotico.id_antibiotico, "A12345")
        self.assertEqual(self.antibiotico.nombre, "Amoxicilina")
        self.assertEqual(self.antibiotico.dosis, 500)
        self.assertEqual(self.antibiotico.tipo_animal, "Bovinos")
        self.assertEqual(self.antibiotico.valor, 100.0)

    def test_modificar_nombre(self):
        self.antibiotico.nombre = "Penicilina"
        self.assertEqual(self.antibiotico.nombre, "Penicilina")

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError):
            self.antibiotico.dosis = 300

        with self.assertRaises(ValueError):
            self.antibiotico.dosis = 700

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            self.antibiotico.tipo_animal = "Caninos"

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.antibiotico.valor = -50.0

    def test_str_representation(self):
        self.assertEqual(str(self.antibiotico), "Amoxicilina (Bovinos) - Dosis: 500Kg - Precio: $100.0")

if __name__ == "__main__":
    unittest.main()
