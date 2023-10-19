import unittest
from model.controldeplagas import ControlDePlagas

class TestControlDePlagas(unittest.TestCase):

    def setUp(self):
        self.producto_plagas = ControlDePlagas("R-001", "Diaria", 150.0, "ControlPlagaEspecial", "P12345", 7)

    def test_inicializacion_control_plagas(self):
        self.assertEqual(self.producto_plagas.registro_ICA, "R-001")
        self.assertEqual(self.producto_plagas.frecuencia_aplicacion, "Diaria")
        self.assertEqual(self.producto_plagas.valor, 150.0)
        self.assertEqual(self.producto_plagas.nombre_producto, "ControlPlagaEspecial")
        self.assertEqual(self.producto_plagas.id_producto, "P12345")
        self.assertEqual(self.producto_plagas.periodo_carencia, 7)

    def test_modificar_periodo_carencia(self):
        self.producto_plagas.periodo_carencia = 10
        self.assertEqual(self.producto_plagas.periodo_carencia, 10)

    def test_str_representation(self):
        expected_string = "ControlPlagaEspecial - Registro ICA: R-001 - Frecuencia: Diaria - Precio: $150.0 - Periodo de Carencia: 7 días"
        self.assertEqual(str(self.producto_plagas), expected_string)

if __name__ == "__main__":
    unittest.main()
