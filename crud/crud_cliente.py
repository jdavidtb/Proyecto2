from model.cliente import Cliente


class CRUDCliente:
    _clientes = []

    @classmethod
    def create_cliente(cls, nombre, cedula):

        nuevo_cliente = Cliente(nombre, cedula)
        cls._clientes.append(nuevo_cliente)
        return nuevo_cliente

    @classmethod
    def read_cliente(cls, cedula):

        for cliente in cls._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    @classmethod
    def update_cliente(cls, cedula, nuevo_nombre=None):

        cliente = cls.read_cliente(cedula)
        if cliente:
            if nuevo_nombre:
                cliente.nombre = nuevo_nombre
            return True
        return False

    @classmethod
    def delete_cliente(cls, cedula):

        cliente = cls.read_cliente(cedula)
        if cliente:
            cls._clientes.remove(cliente)
            return True
        return False

