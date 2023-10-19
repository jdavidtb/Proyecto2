from model.control_de_plagas import ControlDePlagas
from crud.crud_control_de_plagas import ControlDePlagasCRUD

class UIControlDePlagas:

    def __init__(self):
        self.crud = ControlDePlagasCRUD()

    def menu(self):
        while True:
            print("\n--- Menú de Control de Plagas ---")
            print("1. Crear Control de Plagas")
            print("2. Leer Control de Plagas")
            print("3. Actualizar Control de Plagas")
            print("4. Eliminar Control de Plagas")
            print("5. Listar Todos los Controles de Plagas")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.create_control()
            elif opcion == "2":
                self.read_control()
            elif opcion == "3":
                self.update_control()
            elif opcion == "4":
                self.delete_control()
            elif opcion == "5":
                self.list_all_controles()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

    def create_control(self):
        registro_ICA = input("Ingrese el registro ICA del control: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación: ")
        try:
            valor = float(input("Ingrese el valor del control: "))
        except ValueError:
            print("Valor no válido. Debe ser un número.")
            return
        nombre_producto = input("Ingrese el nombre del control: ")
        id_producto = input("Ingrese el ID del control: ")
        try:
            periodo_carencia = int(input("Ingrese el período de carencia en días: "))
        except ValueError:
            print("Período no válido. Debe ser un número entero.")
            return

        control = ControlDePlagas(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto, periodo_carencia)
        self.crud.create(control)
        print(f"Control {nombre_producto} creado con éxito.")

    def read_control(self):
        id_producto = input("Ingrese el ID del control que desea consultar: ")
        control = self.crud.read(id_producto)
        if control:
            print(control)
        else:
            print("Control de plagas no encontrado.")

    def update_control(self):
        id_producto = input("Ingrese el ID del control que desea actualizar: ")
        control = self.crud.read(id_producto)
        if not control:
            print("Control de plagas no encontrado.")
            return

        nuevo_registro_ICA = input(f"Ingrese el nuevo registro ICA (actual '{control.registro_ICA}'): ")
        nueva_frecuencia = input(f"Ingrese la nueva frecuencia (actual '{control.frecuencia_aplicacion}'): ")
        try:
            nuevo_valor = float(input(f"Ingrese el nuevo valor (actual '{control.valor}'): "))
        except ValueError:
            print("Valor no válido. Debe ser un número.")
            return
        nuevo_nombre_producto = input(f"Ingrese el nuevo nombre del control (actual '{control.nombre_producto}'): ")
        try:
            nuevo_periodo_carencia = int(input(f"Ingrese el nuevo período de carencia en días (actual '{control.periodo_carencia} días'): "))
        except ValueError:
            print("Período no válido. Debe ser un número entero.")
            return

        if nuevo_registro_ICA:
            control.registro_ICA = nuevo_registro_ICA
        if nueva_frecuencia:
            control.frecuencia_aplicacion = nueva_frecuencia
        if nuevo_valor:
            control.valor = nuevo_valor
        if nuevo_nombre_producto:
            control.nombre_producto = nuevo_nombre_producto
        if nuevo_periodo_carencia:
            control.periodo_carencia = nuevo_periodo_carencia

        self.crud.update(id_producto, control)
        print(f"Control {control.nombre_producto} actualizado con éxito.")

    def delete_control(self):
        id_producto = input("Ingrese el ID del control que desea eliminar: ")
        result = self.crud.delete(id_producto)
        if result:
            print(f"Control con ID {id_producto} eliminado con éxito.")
        else:
            print("Control de plagas no encontrado.")

    def list_all_controles(self):
        controles = self.crud.list_all()
        if controles:
            for control in controles:
                print(control)
        else:
            print("No hay controles de plagas registrados.")

if __name__ == "__main__":
    ui = UIControlDePlagas()
    ui.menu()

