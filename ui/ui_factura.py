from crud.crud_factura import CRUDFactura
from datetime import datetime


class FacturaUI:

    def main(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.mostrar_facturas()
            elif choice == "2":
                self.agregar_factura()
            elif choice == "3":
                self.editar_factura()
            elif choice == "4":
                self.eliminar_factura()
            elif choice == "5":
                break
            else:
                print("Opción no válida.")

    def menu(self):
        print("\nMENU DE FACTURAS")
        print("1. Mostrar todas las facturas")
        print("2. Agregar factura")
        print("3. Editar factura")
        print("4. Eliminar factura")
        print("5. Salir")
        return input("Seleccione una opción: ")

    def mostrar_facturas(self):
        facturas = CRUDFactura._facturas
        if not facturas:
            print("No hay facturas registradas.")
            return
        for factura in facturas:
            print(
                f"ID: {factura.IDfactura}, Fecha: {factura.fecha}, Valor Total: ${factura.valor_total}, Cédula: {factura.cedula}")

    def agregar_factura(self):
        IDfactura = input("Ingrese el ID de la factura: ")
        fecha_str = input("Ingrese la fecha (YYYY-MM-DD) o presione enter para usar la fecha actual: ")
        fecha = None if not fecha_str else datetime.strptime(fecha_str, '%Y-%m-%d')
        valor_total = float(input("Ingrese el valor total de la factura: "))
        cedula = input("Ingrese la cédula asociada a la factura: ")

        factura = CRUDFactura.create_factura(IDfactura, fecha, valor_total, cedula)
        print(f"Factura {factura.IDfactura} creada exitosamente.")

    def editar_factura(self):
        IDfactura = input("Ingrese el ID de la factura que desea editar: ")
        factura = CRUDFactura.read_factura(IDfactura)
        if not factura:
            print("No se encontró la factura.")
            return

        nueva_fecha_str = input("Ingrese la nueva fecha (YYYY-MM-DD) o presione enter para mantener la actual: ")
        nueva_fecha = None if not nueva_fecha_str else datetime.strptime(nueva_fecha_str, '%Y-%m-%d')
        nuevo_valor_total = input("Ingrese el nuevo valor total o presione enter para mantener el actual: ")
        nuevo_valor_total = float(nuevo_valor_total) if nuevo_valor_total else None
        nueva_cedula = input("Ingrese la nueva cédula o presione enter para mantener la actual: ")

        CRUDFactura.update_factura(IDfactura, nueva_fecha, nuevo_valor_total, nueva_cedula)
        print(f"Factura {IDfactura} actualizada exitosamente.")

    def eliminar_factura(self):
        IDfactura = input("Ingrese el ID de la factura que desea eliminar: ")
        if CRUDFactura.delete_factura(IDfactura):
            print(f"Factura {IDfactura} eliminada exitosamente.")
        else:
            print("No se encontró la factura.")


if __name__ == "__main__":
    ui = FacturaUI()
    ui.main()
