class ProductoControl:
    def __init__(self, registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto):
        self._registro_ICA = registro_ICA
        self._frecuencia_aplicacion = frecuencia_aplicacion
        self._valor = valor
        self._nombre_producto = nombre_producto
        self._id_producto = id_producto

    @property
    def registro_ICA(self):
        return self._registro_ICA

    @registro_ICA.setter
    def registro_ICA(self, registro):
        self._registro_ICA = registro

    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia):
        self._frecuencia_aplicacion = frecuencia

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor >= 0:
            self._valor = valor
        else:
            raise ValueError("El valor debe ser positivo")

    @property
    def nombre_producto(self):
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre):
        self._nombre_producto = nombre

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_prod):
        self._id_producto = id_prod

    def __str__(self):
        return f"{self._nombre_producto} - Registro ICA: {self._registro_ICA} - Frecuencia: {self._frecuencia_aplicacion} - Precio: ${self._valor}"




