def ver_pedidos(conexion):
    # Validamos que la conexión esté activa
    if not conexion:
        print("Error: No hay conexion a la base de datos.")
        return

    print("\n--- LISTADO DE PEDIDOS ---")
    cursor = conexion.cursor()
    
    # Consulta SQL para traer todos los pedidos
    sql = "SELECT idPedidoVenta, fechaPedido, tipoPedido, totalPedido, Usuario_idUsuario, Mesa_idMesa, EstadoPedido_idEstado FROM PedidoVenta"
    
    try:
        cursor.execute(sql)
        pedidos = cursor.fetchall() # Obtiene todos los registros
        
        # Validamos si la tabla está vacía
        if len(pedidos) == 0:
            print("No hay pedidos registrados en este momento.")
        else:
            # Imprimimos la cabecera de nuestra "tabla" en consola
            print(f"{'ID':<5} | {'Fecha':<20} | {'Tipo':<12} | {'Total':<12} | {'Usuario':<8} | {'Mesa':<6} | {'Estado':<7}")
            print("-" * 85)
            
            # Recorremos cada pedido y lo imprimimos con el mismo formato
            for p in pedidos:
                id_pedido = p[0]
                # Convertimos la fecha a texto, si existe
                fecha = p[1].strftime("%Y-%m-%d %H:%M") if p[1] else "Sin fecha"
                tipo = p[2]
                total = f"${p[3]:.2f}"
                usuario = p[4]
                # Si la mesa es None (NULL), mostramos "N/A"
                mesa = p[5] if p[5] is not None else "N/A"
                estado = p[6]
                
                print(f"{id_pedido:<5} | {fecha:<20} | {tipo:<12} | {total:<12} | {usuario:<8} | {mesa:<6} | {estado:<7}")
                
    except Exception as e:
        print(f"Error al consultar los pedidos: {e}")
        
    finally:
        # Cerramos el cursor, pero mantenemos la conexión abierta
        cursor.close()