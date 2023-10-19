class PedidosAntibioticos:
    def __init__(self, IDFactura, Cantidad, IDAntibiotico, Subtotal=None):
        self._IDFactura = IDFactura
        self._Cantidad = Cantidad
        self._IDAntibiotico = IDAntibiotico
        self._Subtotal = Subtotal if Subtotal is not None else 0  # Puedes calcularlo basado en el precio del antibiótico y la cantidad si lo deseas

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
    def IDAntibiotico(self):
        return self._IDAntibiotico

    @IDAntibiotico.setter
    def IDAntibiotico(self, value):
        # Aquí puedes agregar validaciones para el IDAntibiotico si es necesario
        self._IDAntibiotico = value

    @property
    def Subtotal(self):
        return self._Subtotal

    @Subtotal.setter
    def Subtotal(self, value):
        if value < 0:
            raise ValueError("El subtotal no puede ser negativo.")
        self._Subtotal = value

    # Si tienes un método para obtener el precio del antibiótico por su ID, puedes calcular el subtotal así:
    # def calcular_subtotal(self, precio_antibiotico):
    #     self._Subtotal = self._Cantidad * precio_antibiotico
