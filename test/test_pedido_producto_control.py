import unittest
from model.pedido_producto_control import PedidosProductosControl

class TestPedidosProductosControl(unittest.TestCase):

    def setUp(self):
        self.pedido = PedidosProductosControl("F12345", 5, "P12345")

    def test_inicializacion_pedido(self):
        self.assertEqual(self.pedido.IDFactura, "F12345")
        self.assertEqual(self.pedido.Cantidad, 5)
        self.assertEqual(self.pedido.IDProducto, "P12345")
        self.assertEqual(self.pedido.Subtotal, 0)

    def test_modificar_IDFactura(self):
        self.pedido.IDFactura = "F67890"
        self.assertEqual(self.pedido.IDFactura, "F67890")

    def test_modificar_IDProducto(self):
        self.pedido.IDProducto = "P67890"
        self.assertEqual(self.pedido.IDProducto, "P67890")

    def test_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            self.pedido.Cantidad = -5

        with self.assertRaises(ValueError):
            self.pedido.Cantidad = 0

    def test_subtotal_negativo(self):
        with self.assertRaises(ValueError):
            self.pedido.Subtotal = -100.0



if __name__ == "__main__":
    unittest.main()
