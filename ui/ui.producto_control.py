from model.producto_control import ProductoControl
from crud.crud_producto_control import ProductoControlCRUD

class UIProductoControl:

    def __init__(self):
        self.crud = ProductoControlCRUD()

    def menu(self):
        while True:
            print("\n--- Menú de Control de Productos ---")
            print("1. Crear Producto")
            print("2. Leer Producto")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Listar Todos los Productos")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.create_producto()
            elif opcion == "2":
                self.read_producto()
            elif opcion == "3":
                self.update_producto()
            elif opcion == "4":
                self.delete_producto()
            elif opcion == "5":
                self.list_all_productos()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

    def create_producto(self):
        registro_ICA = input("Ingrese el registro ICA del producto: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación: ")
        try:
            valor = float(input("Ingrese el valor del producto: "))
        except ValueError:
            print("Valor no válido. Debe ser un número.")
            return
        nombre_producto = input("Ingrese el nombre del producto: ")
        id_producto = input("Ingrese el ID del producto: ")

        producto = ProductoControl(registro_ICA, frecuencia_aplicacion, valor, nombre_producto, id_producto)
        self.crud.create(producto)
        print(f"Producto {nombre_producto} creado con éxito.")

    def read_producto(self):
        id_producto = input("Ingrese el ID del producto que desea consultar: ")
        producto = self.crud.read(id_producto)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def update_producto(self):
        id_producto = input("Ingrese el ID del producto que desea actualizar: ")
        producto = self.crud.read(id_producto)
        if not producto:
            print("Producto no encontrado.")
            return

        nuevo_registro_ICA = input(f"Ingrese el nuevo registro ICA (actual '{producto.registro_ICA}'): ")
        nueva_frecuencia = input(f"Ingrese la nueva frecuencia (actual '{producto.frecuencia_aplicacion}'): ")
        try:
            nuevo_valor = float(input(f"Ingrese el nuevo valor (actual '{producto.valor}'): "))
        except ValueError:
            print("Valor no válido. Debe ser un número.")
            return
        nuevo_nombre_producto = input(f"Ingrese el nuevo nombre del producto (actual '{producto.nombre_producto}'): ")

        if nuevo_registro_ICA:
            producto.registro_ICA = nuevo_registro_ICA
        if nueva_frecuencia:
            producto.frecuencia_aplicacion = nueva_frecuencia
        if nuevo_valor:
            producto.valor = nuevo_valor
        if nuevo_nombre_producto:
            producto.nombre_producto = nuevo_nombre_producto

        self.crud.update(id_producto, producto)
        print(f"Producto {producto.nombre_producto} actualizado con éxito.")

    def delete_producto(self):
        id_producto = input("Ingrese el ID del producto que desea eliminar: ")
        if self.crud.delete(id_producto):
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado.")

    def list_all_productos(self):
        productos = self.crud.list_all()
        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No hay productos registrados.")
if __name__ == "__main__":
    ui = UIProductoControl()
    ui.menu()