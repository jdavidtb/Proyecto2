import unittest
from model.producto_control import ProductoControl

class TestProductoControl(unittest.TestCase):

    def setUp(self):
        self.producto = ProductoControl("R-001", "Diaria", 150.0, "ControlPlaga", "P12345")

    def test_inicializacion_producto(self):
        self.assertEqual(self.producto.registro_ICA, "R-001")
        self.assertEqual(self.producto.frecuencia_aplicacion, "Diaria")
        self.assertEqual(self.producto.valor, 150.0)
        self.assertEqual(self.producto.nombre_producto, "ControlPlaga")
        self.assertEqual(self.producto.id_producto, "P12345")

    def test_modificar_atributos(self):
        self.producto.registro_ICA = "R-002"
        self.assertEqual(self.producto.registro_ICA, "R-002")

        self.producto.frecuencia_aplicacion = "Semanal"
        self.assertEqual(self.producto.frecuencia_aplicacion, "Semanal")

        self.producto.nombre_producto = "ControlInsecto"
        self.assertEqual(self.producto.nombre_producto, "ControlInsecto")

        self.producto.id_producto = "P12346"
        self.assertEqual(self.producto.id_producto, "P12346")

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.producto.valor = -50.0

    def test_str_representation(self):
        self.assertEqual(str(self.producto), "ControlPlaga - Registro ICA: R-001 - Frecuencia: Diaria - Precio: $150.0")

if __name__ == "__main__":
    unittest.main()
