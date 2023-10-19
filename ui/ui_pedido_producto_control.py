from model.pedido_producto_control import PedidosProductosControl
from crud.crud_pedido_producto_control import CRUDPedidoProductoControl

class PedidoProductoControlUI:

    def menu(self):
        print("Gestión de Pedidos de Productos")
        print("1. Agregar Pedido de Producto")
        print("2. Mostrar Pedido de Producto por IDFactura e IDProducto")
        print("3. Modificar Pedido de Producto")
        print("4. Eliminar Pedido de Producto")
        print("5. Mostrar todos los Pedidos de Productos")
        print("6. Salir")


    def agregar_pedido(self):
        try:
            IDFactura = input("Ingrese el ID de la factura: ")
            Cantidad = int(input("Ingrese la cantidad del producto: "))
            IDProducto = input("Ingrese el ID del producto: ")
            Subtotal = float(input("Ingrese el subtotal (opcional, presione enter para omitir): "))

            pedido = CRUDPedidoProductoControl.create_pedido(IDFactura, Cantidad, IDProducto, Subtotal)
            print(f"Pedido para el producto {pedido.IDProducto} agregado con éxito en la factura {pedido.IDFactura}!")
        except ValueError as e:
            print(e)

    def mostrar_pedido(self):
        IDFactura = input("Ingrese el ID de la factura: ")
        IDProducto = input("Ingrese el ID del producto: ")
        pedido = CRUDPedidoProductoControl.read_pedido(IDFactura, IDProducto)
        if pedido:
            print(f"IDFactura: {pedido.IDFactura}, Cantidad: {pedido.Cantidad}, IDProducto: {pedido.IDProducto}, Subtotal: {pedido.Subtotal}")
        else:
            print("Pedido no encontrado.")

    def modificar_pedido(self):
        try:
            IDFactura = input("Ingrese el ID de la factura que desea modificar: ")
            IDProducto = input("Ingrese el ID del producto que desea modificar: ")
            print("Ingrese los nuevos valores (presione enter para omitir)")
            Cantidad = input("Cantidad: ")
            Subtotal = input("Subtotal: ")

            kwargs = {}
            if Cantidad: kwargs["Cantidad"] = int(Cantidad)
            if Subtotal: kwargs["Subtotal"] = float(Subtotal)

            if CRUDPedidoProductoControl.update_pedido(IDFactura, IDProducto, **kwargs):
                print("Pedido actualizado con éxito!")
            else:
                print("Error al actualizar el pedido.")
        except ValueError as e:
            print(e)

    def eliminar_pedido(self):
        IDFactura = input("Ingrese el ID de la factura que desea eliminar: ")
        IDProducto = input("Ingrese el ID del producto que desea eliminar: ")
        if CRUDPedidoProductoControl.delete_pedido(IDFactura, IDProducto):
            print("Pedido eliminado con éxito!")
        else:
            print("Error al eliminar el pedido.")


    def mostrar_todos(self):
        pedidos = CRUDPedidoProductoControl._pedidos
        for pedido in pedidos:
            print(f"IDFactura: {pedido.IDFactura}, Cantidad: {pedido.Cantidad}, IDProducto: {pedido.IDProducto}, Subtotal: {pedido.Subtotal}")

    def main(self):
        while True:
            self.menu()
            opcion = input("Elija una opción: ")

            if opcion == "1":
                self.agregar_pedido()
            elif opcion == "2":
                self.mostrar_pedido()
            elif opcion == "3":
                self.modificar_pedido()
            elif opcion == "4":
                self.eliminar_pedido()
            elif opcion == "5":
                self.mostrar_todos()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    ui = PedidoProductoControlUI()
    ui.main()


