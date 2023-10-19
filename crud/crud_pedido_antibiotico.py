from model.pedido_antibiotico import PedidosAntibioticos

class CRUDPedidoAntibiotico:

    # Lista temporal para simular una base de datos
    _pedidos_antibioticos = []

    @classmethod
    def create_pedido(cls, IDFactura, Cantidad, IDAntibiotico, Subtotal=None):

        nuevo_pedido = PedidosAntibioticos(IDFactura, Cantidad, IDAntibiotico, Subtotal)
        cls._pedidos_antibioticos.append(nuevo_pedido)
        return nuevo_pedido

    @classmethod
    def read_pedido(cls, IDFactura):

        for pedido in cls._pedidos_antibioticos:
            if pedido.IDFactura == IDFactura:
                return pedido
        return None

    @classmethod
    def update_pedido(cls, IDFactura, nueva_cantidad=None, nuevo_id_antibiotico=None, nuevo_subtotal=None):

        pedido = cls.read_pedido(IDFactura)
        if pedido:
            if nueva_cantidad:
                pedido.Cantidad = nueva_cantidad
            if nuevo_id_antibiotico:
                pedido.IDAntibiotico = nuevo_id_antibiotico
            if nuevo_subtotal is not None:
                pedido.Subtotal = nuevo_subtotal
            return True
        return False

    @classmethod
    def delete_pedido(cls, IDFactura):

        pedido = cls.read_pedido(IDFactura)
        if pedido:
            cls._pedidos_antibioticos.remove(pedido)
            return True
        return False
