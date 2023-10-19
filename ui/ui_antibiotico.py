from model.antibiotico import Antibiotico
from crud.crud_antibiotico import CRUDAntibiotico

class AntibioticoUI:

    def mostrar_menu(self):
        print("Gestión de Antibióticos")
        print("1. Agregar Antibiótico")
        print("2. Mostrar Antibiótico por ID")
        print("3. Modificar Antibiótico")
        print("4. Eliminar Antibiótico")
        print("5. Mostrar todos los Antibióticos")
        print("6. Salir")

    def agregar_antibiotico(self):
        try:
            id_antibiotico = int(input("Ingrese el ID del antibiótico: "))
            nombre = input("Ingrese el nombre del antibiótico: ")
            dosis = float(input("Ingrese la dosis (400Kg a 600Kg): "))
            tipo_animal = input("Ingrese el tipo de animal (Bovinos, Caprinos, Porcinos): ")
            valor = float(input("Ingrese el valor del antibiótico: "))

            antibiotico = CRUDAntibiotico.create_antibiotico(id_antibiotico, dosis, tipo_animal, nombre, valor)
            print(f"Antibiótico {antibiotico.nombre} agregado con éxito!")
        except ValueError as e:
            print(e)

    def mostrar_antibiotico(self):
        id_antibiotico = int(input("Ingrese el ID del antibiótico que desea ver: "))
        antibiotico = CRUDAntibiotico.read_antibiotico(id_antibiotico)
        if antibiotico:
            print(antibiotico)
        else:
            print("Antibiótico no encontrado.")

    def modificar_antibiotico(self):
        try:
            id_antibiotico = int(input("Ingrese el ID del antibiótico que desea modificar: "))
            print("Ingrese los nuevos valores (presione enter para omitir)")
            nombre = input("Nombre: ")
            dosis = input("Dosis: ")
            tipo_animal = input("Tipo de animal: ")
            valor = input("Valor: ")

            kwargs = {}
            if nombre: kwargs["nombre"] = nombre
            if dosis: kwargs["dosis"] = float(dosis)
            if tipo_animal: kwargs["tipo_animal"] = tipo_animal
            if valor: kwargs["valor"] = float(valor)

            if CRUDAntibiotico.update_antibiotico(id_antibiotico, **kwargs):
                print("Antibiótico actualizado con éxito!")
            else:
                print("Error al actualizar el antibiótico.")
        except ValueError as e:
            print(e)

    def eliminar_antibiotico(self):
        id_antibiotico = int(input("Ingrese el ID del antibiótico que desea eliminar: "))
        if CRUDAntibiotico.delete_antibiotico(id_antibiotico):
            print("Antibiótico eliminado con éxito!")
        else:
            print("Error al eliminar el antibiótico.")

    def mostrar_todos(self):
        antibioticos = CRUDAntibiotico._antibioticos
        for antibiotico in antibioticos:
            print(antibiotico)

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elija una opción: ")

            if opcion == "1":
                self.agregar_antibiotico()
            elif opcion == "2":
                self.mostrar_antibiotico()
            elif opcion == "3":
                self.modificar_antibiotico()
            elif opcion == "4":
                self.eliminar_antibiotico()
            elif opcion == "5":
                self.mostrar_todos()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ui = AntibioticoUI()
    ui.main()

