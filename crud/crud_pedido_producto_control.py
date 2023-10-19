from model.pedido_producto_control import PedidosProductosControl

class CRUDPedidoProductoControl:

    _pedidos = []

    @classmethod
    def create_pedido(cls, IDFactura, Cantidad, IDProducto, Subtotal=None):
        pedido = PedidosProductosControl(IDFactura, Cantidad, IDProducto, Subtotal)
        cls._pedidos.append(pedido)
        return pedido

    @classmethod
    def read_pedido(cls, IDFactura, IDProducto):
        for pedido in cls._pedidos:
            if pedido.IDFactura == IDFactura and pedido.IDProducto == IDProducto:
                return pedido
        return None

    @classmethod
    def update_pedido(cls, IDFactura, IDProducto, **kwargs):
        pedido = cls.read_pedido(IDFactura, IDProducto)
        if pedido:
            if "Cantidad" in kwargs:
                pedido.Cantidad = kwargs["Cantidad"]
            if "Subtotal" in kwargs:
                pedido.Subtotal = kwargs["Subtotal"]
            return True
        return False

    @classmethod
    def delete_pedido(cls, IDFactura, IDProducto):
        pedido = cls.read_pedido(IDFactura, IDProducto)
        if pedido:
            cls._pedidos.remove(pedido)
            return True
        return False
