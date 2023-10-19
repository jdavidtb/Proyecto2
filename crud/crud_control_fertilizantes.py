from model.control_fertilizantes import ControlDeFertilizantes

class CRUDControlDeFertilizantes:

    def __init__(self):
        self.fertilizantes = []

    def create(self, registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto, fecha_ultima_aplicacion):
        nuevo_fertilizante = ControlDeFertilizantes(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto, fecha_ultima_aplicacion)
        self.fertilizantes.append(nuevo_fertilizante)
        return nuevo_fertilizante

    def read(self, id_producto):
        for fertilizante in self.fertilizantes:
            if fertilizante.id_producto == id_producto:
                return fertilizante
        return None

    def update(self, id_producto, **kwargs):
        fertilizante = self.read(id_producto)
        if fertilizante:
            if 'registro_ICA' in kwargs:
                fertilizante.registro_ICA = kwargs['registro_ICA']
            if 'frecuencia_aplicacion' in kwargs:
                fertilizante.frecuencia_aplicacion = kwargs['frecuencia_aplicacion']
            if 'valor' in kwargs:
                fertilizante.valor = kwargs['valor']
            if 'nombre_producto' in kwargs:
                fertilizante.nombre_producto = kwargs['nombre_producto']
            if 'fecha_ultima_aplicacion' in kwargs:
                fertilizante.fecha_ultima_aplicacion = kwargs['fecha_ultima_aplicacion']
            return True
        return False

    def delete(self, id_producto):
        fertilizante = self.read(id_producto)
        if fertilizante:
            self.fertilizantes.remove(fertilizante)
            return True
        return False

    def list_all(self):
        return self.fertilizantes
