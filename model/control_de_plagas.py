from producto_control import ProductoControl

class ControlDePlagas(ProductoControl):
    def __init__(self, registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto, periodo_carencia):
        super().__init__(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto)
        self._periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self._periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo):
        self._periodo_carencia = periodo

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Periodo de Carencia: {self._periodo_carencia} días"
