from conexion import conectar
from crear_estado_mesa import crear_tabla_estado_mesa
from crear_mesa import crear_tabla_mesa
from crear_pedido_venta import crear_tabla_pedido_venta
from insertar_estado_mesa import insertar_estado_mesa
from insertar_mesa import insertar_mesa
from agregar_pedido import agregar_pedido
# Importamos todas las funciones del CRUD
from crud_pedido import agregar_pedido, ver_pedidos, actualizar_pedido, eliminar_pedido, ver_mesas

def mostrar_menu():
    print("\n================= MENU CHICKEN BIKER =================")
    print("0. Instalar Base de Datos (Crear y cargar datos iniciales)")
    print("1. Agregar nuevo pedido")
    print("2. Ver todos los pedidos")
    print("3. Actualizar estado de un pedido")
    print("4. Eliminar un pedido")
    print("5. Ver estado de las mesas")
    print("6. Salir")
    print("======================================================")

def main():
    conexion = conectar()
    if not conexion:
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "0":
            crear_tabla_estado_mesa(); crear_tabla_mesa(); crear_tabla_pedido_venta()
            insertar_estado_mesa(); insertar_mesa(); insertar_pedido_venta()
        elif opcion == "1":
            agregar_pedido(conexion)
        elif opcion == "2":
            ver_pedidos(conexion)
        elif opcion == "3":
            actualizar_pedido(conexion)
        elif opcion == "4":
            eliminar_pedido(conexion)
        elif opcion == "5":
            ver_mesas(conexion)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
            
    conexion.close()

if __name__ == "__main__":
    main()