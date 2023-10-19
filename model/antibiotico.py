class Antibiotico:
    def __init__(self, id_antibiotico, dosis, tipo_animal, nombre, valor):
        self._id_antibiotico = id_antibiotico
        self._nombre = nombre
        self._dosis = dosis
        self._tipo_animal = tipo_animal
        self._valor = valor

    @property
    def id_antibiotico(self):
        return self._id_antibiotico

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, dosis):
        if 400 <= dosis <= 600:
            self._dosis = dosis
        else:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")

    @property
    def tipo_animal(self):
        return self._tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo):
        if tipo in ["Bovinos", "Caprinos", "Porcinos"]:
            self._tipo_animal = tipo
        else:
            raise ValueError("Tipo de animal no válido. Debe ser 'Bovinos', 'Caprinos' o 'Porcinos'.")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor >= 0:
            self._valor = valor
        else:
            raise ValueError("El valor debe ser positivo")

    def __str__(self):
        return f"{self._nombre} ({self._tipo_animal}) - Dosis: {self._dosis}Kg - Precio: ${self._valor}"
