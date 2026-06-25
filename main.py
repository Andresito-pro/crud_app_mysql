from conexion import conectar
from crear_estado_mesa import crear_tabla_estado_mesa
from crear_mesa import crear_tabla_mesa
from crear_pedido_venta import crear_tabla_pedido_venta
from insertar_estado_mesa import insertar_estado_mesa
from insertar_mesa import insertar_mesa
from agregar_pedido import agregar_pedido
from eliminar_pedido import eliminar_pedido
from actualizar_pedido import actualizar_pedido
from ver_pedidos import ver_pedidos
from ver_estado_mesas import ver_mesas



def mostrar_menu():
    print("\n================= MENU CHICKEN BIKER =================")
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
        
        if opcion == "1":
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