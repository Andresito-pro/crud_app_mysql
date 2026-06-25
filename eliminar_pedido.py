def eliminar_pedido(conexion):
    # Validamos que la conexión esté activa
    if not conexion:
        print("Error: No hay conexion a la base de datos.")
        return

    print("\n--- ELIMINAR PEDIDO ---")
    
    try:
        id_pedido = int(input("Ingrese el ID del pedido que desea eliminar: "))
        
        # Confirmación de seguridad
        confirmacion = input(f"¿Esta seguro de que desea eliminar el pedido {id_pedido}? (s/n): ")
        
        if confirmacion.lower() != 's':
            print("Operacion cancelada.")
            return
            
        cursor = conexion.cursor()
        sql = "DELETE FROM PedidoVenta WHERE idPedidoVenta = %s"
        
        cursor.execute(sql, (id_pedido,))
        
        if cursor.rowcount > 0:
            conexion.commit()
            print(f"Exito! El pedido {id_pedido} fue eliminado correctamente.")
        else:
            print(f"No se encontro ningun pedido con el ID {id_pedido}.")
            
    except ValueError:
        print("Error: El ID debe ser un numero entero.")
    except Exception as e:
        print(f"Error al eliminar el pedido: {e}")
        conexion.rollback()
    finally:
        if 'cursor' in locals():
            cursor.close()