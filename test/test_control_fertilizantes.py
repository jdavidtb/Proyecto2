import unittest
from datetime import datetime
from model.control_fertilizantes import ControlDeFertilizantes

class TestControlDeFertilizantes(unittest.TestCase):

    def setUp(self):
        self.fertilizante = ControlDeFertilizantes("R-002", "Semanal", 200.0, "FertilizanteEspecial", "F12345", "2023-01-10")

    def test_inicializacion_control_fertilizantes(self):
        self.assertEqual(self.fertilizante.registro_ICA, "R-002")
        self.assertEqual(self.fertilizante.frecuencia_aplicacion, "Semanal")
        self.assertEqual(self.fertilizante.valor, 200.0)
        self.assertEqual(self.fertilizante.nombre_producto, "FertilizanteEspecial")
        self.assertEqual(self.fertilizante.id_producto, "F12345")
        self.assertEqual(self.fertilizante.fecha_ultima_aplicacion, datetime.strptime("2023-01-10", '%Y-%m-%d'))

    def test_modificar_fecha_ultima_aplicacion(self):
        self.fertilizante.fecha_ultima_aplicacion = "2023-02-15"
        self.assertEqual(self.fertilizante.fecha_ultima_aplicacion, datetime.strptime("2023-02-15", '%Y-%m-%d'))

    def test_str_representation(self):
        expected_string = "FertilizanteEspecial - Registro ICA: R-002 - Frecuencia: Semanal - Precio: $200.0 - Fecha de Última Aplicación: 2023-01-10"
        self.assertEqual(str(self.fertilizante), expected_string)

if __name__ == "__main__":
    unittest.main()
