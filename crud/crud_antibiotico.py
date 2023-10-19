from model.antibiotico import Antibiotico

class CRUDAntibiotico:

    _antibioticos = []

    @classmethod
    def create_antibiotico(cls, id_antibiotico, dosis, tipo_animal, nombre, valor):
        antibiotico = Antibiotico(id_antibiotico, dosis, tipo_animal, nombre, valor)
        cls._antibioticos.append(antibiotico)
        return antibiotico

    @classmethod
    def read_antibiotico(cls, id_antibiotico):
        for antibiotico in cls._antibioticos:
            if antibiotico.id_antibiotico == id_antibiotico:
                return antibiotico
        return None

    @classmethod
    def update_antibiotico(cls, id_antibiotico, **kwargs):
        antibiotico = cls.read_antibiotico(id_antibiotico)
        if antibiotico:
            if "nombre" in kwargs:
                antibiotico.nombre = kwargs["nombre"]
            if "dosis" in kwargs:
                antibiotico.dosis = kwargs["dosis"]
            if "tipo_animal" in kwargs:
                antibiotico.tipo_animal = kwargs["tipo_animal"]
            if "valor" in kwargs:
                antibiotico.valor = kwargs["valor"]
            return True
        return False

    @classmethod
    def delete_antibiotico(cls, id_antibiotico):
        antibiotico = cls.read_antibiotico(id_antibiotico)
        if antibiotico:
            cls._antibioticos.remove(antibiotico)
            return True
        return False
