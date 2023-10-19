from model.producto_control import ProductoControl
from model.control_de_plagas import ControlDePlagas


class ControlDePlagasCRUD:

    def __init__(self):
        self._controles = []

    def create(self, control):
        if isinstance(control, ControlDePlagas):
            self._controles.append(control)
        else:
            raise ValueError("El objeto debe ser una instancia de ControlDePlagas.")

    def read(self, id_producto):
        for control in self._controles:
            if control.id_producto == id_producto:
                return control
        return None

    def update(self, id_producto, nuevo_control):
        for i, control in enumerate(self._controles):
            if control.id_producto == id_producto:
                if isinstance(nuevo_control, ControlDePlagas):
                    self._controles[i] = nuevo_control
                    return True
        return False

    def delete(self, id_producto):
        for i, control in enumerate(self._controles):
            if control.id_producto == id_producto:
                del self._controles[i]
                return True
        return False
