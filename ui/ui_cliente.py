from model.cliente import Cliente
from crud.crud_cliente import CRUDCliente
from crud.crud_factura import CRUDFactura

class ClienteUI:

    def menu(self):
        print("\nMENU DE CLIENTES")
        print("1. Mostrar todos los clientes")
        print("2. Agregar cliente")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Buscar cliente por cédula")
        print("6. Salir")
        return input("Seleccione una opción: ")


    def main(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.mostrar_clientes()
            elif choice == "2":
                self.agregar_cliente()
            elif choice == "3":
                cedula = input("Ingrese la cédula del cliente a editar: ")
                self.editar_cliente(cedula)
            elif choice == "4":
                cedula = input("Ingrese la cédula del cliente a eliminar: ")
                self.eliminar_cliente(cedula)
            elif choice == "5":
                self.buscar_por_cedula()
            elif choice == "6":
                break
            else:
                print("Opción no válida.")


    def mostrar_clientes(self):
        lista_clientes = CRUDCliente._clientes
        for cliente in lista_clientes:
            print(cliente.nombre, cliente.cedula)

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        CRUDCliente.create_cliente(nombre, cedula)
        print("Cliente agregado exitosamente!")

    def editar_cliente(self, cedula):
        cliente = CRUDCliente.read_cliente(cedula)
        if cliente:
            nuevo_nombre = input(f"Editar nombre de {cliente.nombre} (deje en blanco para mantener): ")
            if nuevo_nombre:
                CRUDCliente.update_cliente(cedula, nuevo_nombre)
                print("Cliente actualizado exitosamente!")
            else:
                print("No se hicieron cambios.")
        else:
            print("Cliente no encontrado.")

    def eliminar_cliente(self, cedula):
        eliminado = CRUDCliente.delete_cliente(cedula)
        if eliminado:
            print("Cliente eliminado exitosamente!")
        else:
            print("Cliente no encontrado.")

    def buscar_por_cedula(self):
        cedula = input("Ingrese la cédula del cliente: ")
        cliente = CRUDCliente.read_cliente(cedula)

        if cliente:
            print(f"Cliente: {cliente.nombre}")
            if cliente.facturas:
                print("Facturas asociadas:")
                for factura in cliente.facturas:
                    print(f"Factura ID: {factura.id}, Fecha: {factura.fecha}")

                    # Obtener y mostrar los productos de la factura
                    productos = CRUDFactura.obtener_productos(factura.id)
                    for producto in productos:
                        print(f"   - Producto: {producto.nombre}, Cantidad: {producto.cantidad}")
            else:
                print("El cliente no tiene facturas asociadas.")
        else:
            print("No se encontró un cliente con esa cédula.")

if __name__ == "__main__":
    ui = ClienteUI()
    ui.main()
