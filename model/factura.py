from datetime import datetime

class Factura:
    def __init__(self, valor_total, cedula, id_factura, fecha=None):
        self._id_factura = id_factura
        self._valor_total = valor_total
        self._cedula = cedula
        self._productos_control = []
        self._antibiotico = []

        if fecha is None:
            self._fecha = datetime.now()
        else:
            self.fecha = fecha

    @property
    def id_factura(self):
        return self._id_factura

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El valor total debe ser numérico.")
        if value < 0:
            raise ValueError("El valor total no puede ser negativo.")
        self._valor_total = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        if not value.isdigit():
            raise ValueError("La cédula debe contener solo números.")
        if len(value) == 0:
            raise ValueError("La cédula no puede estar vacía.")
        self._cedula = value

    def agregar_pedido_control(self, producto_control):
        self._productos_control.append(producto_control)
        self.calcular_valor_total()

    def agregar_pedido_antibiotico(self, antibiotico):
        self._antibiotico.append(antibiotico)
        self.calcular_valor_total()

    def calcular_valor_total(self):
        total_productos_control = sum(item.valor for item in self._productos_control)
        total_antibioticos = sum(item.valor for item in self._antibiotico)
        self._valor_total = total_productos_control + total_antibioticos

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if isinstance(valor, datetime):
            self._fecha = valor
        else:
            raise ValueError("La fecha proporcionada debe ser un objeto datetime.")

    @id_factura.setter
    def id_factura(self, value):
        self._id_factura = value

    def __str__(self):
        return f"Factura del {self.fecha} con valor total de {self._valor_total}"

