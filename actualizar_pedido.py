def actualizar_pedido(conexion):
    # Validamos que la conexión esté activa
    if not conexion:
        print("Error: No hay conexion a la base de datos.")
        return

    print("\n--- ACTUALIZAR PEDIDO ---")
    
    try:
        id_pedido = int(input("Ingrese el ID del pedido que desea actualizar: "))
        
        print("Nota: Deje el espacio en blanco y presione Enter si no desea cambiar el dato.")
        nuevo_estado = input("Nuevo ID del Estado del Pedido: ")
        nueva_mesa = input("Nuevo ID de la Mesa (escriba '0' para volverlo 'Para llevar'): ")
        
        # Preparamos las partes de la consulta SQL dependiendo de lo que el usuario escribió
        campos_a_actualizar = []
        valores = []
        
        if nuevo_estado.strip() != "":
            campos_a_actualizar.append("EstadoPedido_idEstado = %s")
            valores.append(int(nuevo_estado))
            
        if nueva_mesa.strip() != "":
            if nueva_mesa == "0":
                campos_a_actualizar.append("Mesa_idMesa = NULL")
            else:
                campos_a_actualizar.append("Mesa_idMesa = %s")
                valores.append(int(nueva_mesa))
                
        # Validamos si el usuario no ingresó nada
        if len(campos_a_actualizar) == 0:
            print("No se ingresaron datos nuevos. Operacion cancelada.")
            return
            
        # Construimos la consulta SQL final uniendo los campos
        sql = f"UPDATE PedidoVenta SET {', '.join(campos_a_actualizar)} WHERE idPedidoVenta = %s"
        valores.append(id_pedido) # Añadimos el ID al final de la lista de valores
        
        cursor = conexion.cursor()
        cursor.execute(sql, tuple(valores))
        
        # Validamos si realmente se afectó alguna fila (si el ID existía)
        if cursor.rowcount > 0:
            conexion.commit()
            print(f"Exito! El pedido {id_pedido} ha sido actualizado.")
        else:
            print(f"No se encontro ningun pedido con el ID {id_pedido}.")
            
    except ValueError:
        print("Error: Los IDs deben ser numeros enteros.")
    except Exception as e:
        print(f"Error al actualizar el pedido: {e}")
        conexion.rollback()
    finally:
        # Validamos que la variable cursor exista antes de intentar cerrarla
        if 'cursor' in locals():
            cursor.close()