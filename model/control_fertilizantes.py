from producto_control import ProductoControl
from datetime import datetime

class ControlDeFertilizantes(ProductoControl):
    def __init__(self, registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto, fecha_ultima_aplicacion):
        super().__init__(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto)
        self._fecha_ultima_aplicacion = datetime.strptime(fecha_ultima_aplicacion, '%Y-%m-%d') if isinstance(fecha_ultima_aplicacion, str) else fecha_ultima_aplicacion

    @property
    def fecha_ultima_aplicacion(self):
        return self._fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, fecha):
        self._fecha_ultima_aplicacion = datetime.strptime(fecha, '%Y-%m-%d') if isinstance(fecha, str) else fecha

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Fecha de Última Aplicación: {self._fecha_ultima_aplicacion.strftime('%Y-%m-%d')}"
