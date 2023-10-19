from model.control_fertilizantes import ControlDeFertilizantes
from crud.crud_control_fertilizantes import CRUDControlDeFertilizantes


class FertilizantesUI:

    def __init__(self):
        self.crud = CRUDControlDeFertilizantes()

    def start(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.add_fertilizante()
            elif choice == "2":
                self.view_fertilizante()
            elif choice == "3":
                self.update_fertilizante()
            elif choice == "4":
                self.delete_fertilizante()
            elif choice == "5":
                self.list_all()
            elif choice == "6":
                break
            else:
                print("Opción no válida.")

    def menu(self):
        print("\nMENU DE FERTILIZANTES")
        print("1. Añadir Fertilizante")
        print("2. Ver Fertilizante por ID")
        print("3. Actualizar Fertilizante")
        print("4. Eliminar Fertilizante")
        print("5. Listar todos los Fertilizantes")
        print("6. Salir")
        return input("Seleccione una opción: ")

    def add_fertilizante(self):
        registro_ICA = input("Ingrese el Registro ICA: ")
        frecuencia_aplicacion = input("Ingrese la Frecuencia de Aplicación: ")
        valor = float(input("Ingrese el Valor: "))
        nombre_producto = input("Ingrese el Nombre del Producto: ")
        id_producto = input("Ingrese el ID del Producto: ")
        fecha_ultima_aplicacion = input("Ingrese la Fecha de Última Aplicación (YYYY-MM-DD): ")
        self.crud.create(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto,
                         fecha_ultima_aplicacion)
        print("Fertilizante añadido con éxito.")

    def view_fertilizante(self):
        id_producto = input("Ingrese el ID del Producto a buscar: ")
        fertilizante = self.crud.read(id_producto)
        if fertilizante:
            print(fertilizante)
        else:
            print("Fertilizante no encontrado.")

    def update_fertilizante(self):
        id_producto = input("Ingrese el ID del Producto a actualizar: ")
        kwargs = {}
        attrs = ["registro_ICA", "frecuencia_aplicacion", "valor", "nombre_producto", "fecha_ultima_aplicacion"]
        for attr in attrs:
            val = input(f"Ingrese nuevo valor para {attr} (deje en blanco para no cambiar): ")
            if val:
                kwargs[attr] = val

        updated = self.crud.update(id_producto, **kwargs)
        if updated:
            print("Fertilizante actualizado con éxito.")
        else:
            print("Fertilizante no encontrado.")

    def delete_fertilizante(self):
        id_producto = input("Ingrese el ID del Producto a eliminar: ")
        deleted = self.crud.delete(id_producto)
        if deleted:
            print("Fertilizante eliminado con éxito.")
        else:
            print("Fertilizante no encontrado.")

    def list_all(self):
        fertilizantes = self.crud.list_all()
        for fert in fertilizantes:
            print(fert)


if __name__ == "__main__":
    ui = FertilizantesUI()
    ui.start()
