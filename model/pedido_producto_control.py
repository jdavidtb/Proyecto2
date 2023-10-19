class PedidosProductosControl:
    def __init__(self, IDFactura, Cantidad, IDProducto, Subtotal=None):
        self._IDFactura = IDFactura
        self._Cantidad = Cantidad
        self._IDProducto = IDProducto
        self._Subtotal = Subtotal if Subtotal is not None else 0  # Puedes calcularlo basado en el precio del producto y la cantidad si lo deseas

    @property
    def IDFactura(self):
        return self._IDFactura

    @IDFactura.setter
    def IDFactura(self, value):
        self._IDFactura = value

    @property
    def Cantidad(self):
        return self._Cantidad

    @Cantidad.setter
    def Cantidad(self, value):
        if value <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self._Cantidad = value

    @property
    def IDProducto(self):
        return self._IDProducto

    @IDProducto.setter
    def IDProducto(self, value):
        self._IDProducto = value

    @property
    def Subtotal(self):
        return self._Subtotal

    @Subtotal.setter
    def Subtotal(self, value):
        if value < 0:
            raise ValueError("El subtotal no puede ser negativo.")
        self._Subtotal = value
