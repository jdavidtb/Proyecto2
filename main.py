from ui.ui_factura import FacturaUI
from ui.ui_cliente import ClienteUI
from ui.ui_antibiotico import AntibioticoUI
from ui.ui_producto_control import UIProductoControl
from ui.ui_control_de_plagas import UIControlDePlagas
from ui.ui_control_fertilizantes import FertilizantesUI


def main_menu():
    while True:
        print("\nMENU PRINCIPAL DE TIENDA AGRÍCOLA")
        print("1. Cliente ")
        print("2. Factura")
        print("3. Producto Control")
        print("4. Antibióticos")
        print("5. Control de Plagas")
        print("6. Control de Fertilizantes")
        print("7. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            cliente_ui =ClienteUI ()
            cliente_ui.main()
        elif choice == "2":
            factura_ui = FacturaUI()
            factura_ui.main()

            pass
        elif choice == "3":
            producto_control_ui =UIProductoControl()
            producto_control_ui.main()
            pass
        elif choice == "4":
            antibiotico_ui = AntibioticoUI()
            antibiotico_ui.main()
            pass
        elif choice == "5":
            control_plagas_ui= UIControlDePlagas()
            control_plagas_ui.main()
            pass
        elif choice == "6":
            control_fertilizantes= FertilizantesUI()
            control_fertilizantes.main()
            pass
        elif choice == "7":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main_menu()
