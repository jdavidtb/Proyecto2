class Cliente:
    def __init__(self, nombre, cedula):
        self._nombre = nombre
        self._cedula = cedula
        self._facturas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

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
    def facturas(self):
        return self._facturas

    def agregar_factura(self, factura):
        self._facturas.append(factura)