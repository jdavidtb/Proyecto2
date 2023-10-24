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
                f"ID: {factura.id_factura}, Fecha: {factura.fecha}, Valor Total: ${factura.valor_total}, Cédula: {factura.cedula}")

    def agregar_factura(self):
        id_factura = input("Ingrese el ID de la factura: ")

        try:
            fecha_str = input("Ingrese la fecha (YYYY-MM-DD) o presione enter para usar la fecha actual: ")
            fecha = None if not fecha_str else datetime.strptime(fecha_str, '%Y-%m-%d')
            valor_total = float(input("Ingrese el valor total de la factura: "))
        except ValueError:
            print("Formato de entrada no válido.")
            return

        cedula = input("Ingrese la cédula asociada a la factura: ")

        factura = CRUDFactura.create_factura(id_factura, fecha, valor_total, cedula)
        print(f"Factura {factura.id_factura} creada exitosamente.")

    def editar_factura(self):
        id_factura = input("Ingrese el ID de la factura que desea editar: ")
        factura = CRUDFactura.read_factura(id_factura)
        if not factura:
            print("No se encontró la factura.")
            return

        nueva_fecha_str = input("Ingrese la nueva fecha (YYYY-MM-DD) o presione enter para mantener la actual: ")
        if nueva_fecha_str:
            try:
                nueva_fecha = datetime.strptime(nueva_fecha_str, '%Y-%m-%d')
            except ValueError:
                print("Formato de fecha no válido.")
                return
        else:
            nueva_fecha = factura.fecha

        nuevo_valor_str = input("Ingrese el nuevo valor total o presione enter para mantener el actual: ")
        if nuevo_valor_str:
            try:
                nuevo_valor_total = float(nuevo_valor_str)
            except ValueError:
                print("Valor total no válido.")
                return
        else:
            nuevo_valor_total = factura.valor_total

        nueva_cedula = input("Ingrese la nueva cédula o presione enter para mantener la actual: ")
        nueva_cedula = nueva_cedula if nueva_cedula else factura.cedula

        CRUDFactura.update_factura(id_factura, nueva_valor_total, nueva_fecha)
        print(f"Factura {id_factura} actualizada exitosamente.")

    def eliminar_factura(self):
        id_factura = input("Ingrese el ID de la factura que desea eliminar: ")
        if CRUDFactura.delete_factura(id_factura):
            print(f"Factura {id_factura} eliminada exitosamente.")
        else:
            print("No se encontró la factura.")


if __name__ == "__main__":
    ui = FacturaUI()
    ui.main()
