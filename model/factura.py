from datetime import datetime


class Factura:
    def __init__(self, valor_total, cedula, id_factura, fecha=None):
        self._id_factura = id_factura
        self._valor_total = valor_total
        self._cedula = cedula
        self._pedidos = []

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

    @property
    def pedidos(self):
        return self._pedidos

    def agregar_pedido(self, pedido):
        self._pedidos.append(pedido)
        self.calcular_valor_total()

    def calcular_valor_total(self):
        self._valor_total = sum(pedido.subtotal for pedido in self._pedidos)

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if isinstance(valor, datetime):
            self._fecha = valor
        else:
            raise ValueError("La fecha proporcionada debe ser un objeto datetime.")

    def __str__(self):
        return f"Factura del {self.fecha} con valor total de {self._valor_total}"
