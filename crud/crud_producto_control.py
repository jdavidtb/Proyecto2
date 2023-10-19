from model.producto_control import ProductoControl

class ProductoControlCRUD:

    def __init__(self):
        self._productos = []

    def create(self, producto):
        if isinstance(producto, ProductoControl):
            self._productos.append(producto)
        else:
            raise ValueError("El objeto debe ser una instancia de ProductoControl.")

    def read(self, id_producto):
        for producto in self._productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def update(self, id_producto, nuevo_producto):
        for i, producto in enumerate(self._productos):
            if producto.id_producto == id_producto:
                if isinstance(nuevo_producto, ProductoControl):
                    self._productos[i] = nuevo_producto
                    return True
        return False

    def delete(self, id_producto):
        for i, producto in enumerate(self._productos):
            if producto.id_producto == id_producto:
                del self._productos[i]
                return True
        return False

    def list_all(self):
        return self._productos
