from model.pedido_antibiotico import PedidosAntibioticos
from crud.crud_pedido_antibiotico import CRUDPedidoAntibiotico

class PedidoAntibioticoUI:

    def mostrar_menu(self):
        print("\n-- Menú de Pedidos de Antibióticos --")
        print("1. Agregar nuevo pedido")
        print("2. Consultar pedido por ID de factura")
        print("3. Actualizar pedido")
        print("4. Eliminar pedido")
        print("5. Salir")

    def agregar_pedido(self):
        IDFactura = int(input("Ingrese ID de factura: "))
        Cantidad = int(input("Ingrese cantidad: "))
        IDAntibiotico = int(input("Ingrese ID del antibiótico: "))
        Subtotal = None

        pedido = CRUDPedidoAntibiotico.create_pedido(IDFactura, Cantidad, IDAntibiotico, Subtotal)
        print(f"Pedido creado con éxito: {pedido}")

    def consultar_pedido(self):
        IDFactura = int(input("Ingrese ID de factura: "))
        pedido = CRUDPedidoAntibiotico.read_pedido(IDFactura)

        if pedido:
            print(pedido)
        else:
            print("Pedido no encontrado.")

    def actualizar_pedido(self):
        IDFactura = int(input("Ingrese ID de factura: "))
        nueva_cantidad = int(input("Ingrese nueva cantidad: "))
        nuevo_id_antibiotico = int(input("Ingrese nuevo ID del antibiótico: "))
        nuevo_subtotal = None

        if CRUDPedidoAntibiotico.update_pedido(IDFactura, nueva_cantidad, nuevo_id_antibiotico, nuevo_subtotal):
            print("Pedido actualizado con éxito.")
        else:
            print("Pedido no encontrado.")

    def eliminar_pedido(self):
        IDFactura = int(input("Ingrese ID de factura: "))
        if CRUDPedidoAntibiotico.delete_pedido(IDFactura):
            print("Pedido eliminado con éxito.")
        else:
            print("Pedido no encontrado.")

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_pedido()
            elif opcion == "2":
                self.consultar_pedido()
            elif opcion == "3":
                self.actualizar_pedido()
            elif opcion == "4":
                self.eliminar_pedido()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")


# Uso de la UI
if __name__ == "__main__":
    ui = PedidoAntibioticoUI()
    ui.main()
