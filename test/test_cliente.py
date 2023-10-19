import unittest
from model.cliente import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Juan", "1234567890")

    def test_inicializacion_cliente(self):
        self.assertEqual(self.cliente.nombre, "Juan")
        self.assertEqual(self.cliente.cedula, "1234567890")
        self.assertEqual(len(self.cliente.facturas), 0)

    def test_modificar_nombre(self):
        self.cliente.nombre = "Pedro"
        self.assertEqual(self.cliente.nombre, "Pedro")

    def test_modificar_cedula(self):
        self.cliente.cedula = "0987654321"
        self.assertEqual(self.cliente.cedula, "0987654321")

    def test_cedula_no_numeros(self):
        with self.assertRaises(ValueError):
            self.cliente.cedula = "abcd1234"

    def test_cedula_vacia(self):
        with self.assertRaises(ValueError):
            self.cliente.cedula = ""

    def test_agregar_factura(self):
        factura_mock = "factura_mock"
        self.cliente.agregar_factura(factura_mock)
        self.assertEqual(len(self.cliente.facturas), 1)
        self.assertEqual(self.cliente.facturas[0], factura_mock)

if __name__ == "__main__":
    unittest.main()
