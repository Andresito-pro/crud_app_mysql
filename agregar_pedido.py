from datetime import datetime

def agregar_pedido(conexion):
    # Validamos que la conexión esté activa
    if not conexion:
        print("Error: No hay conexion a la base de datos.")
        return

    print("\n--- AGREGAR NUEVO PEDIDO ---")
    
    # Generamos la fecha actual automáticamente
    fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fecha y hora del pedido: {fecha_pedido}")
    
    # Capturamos los datos en texto
    tipo_pedido = input("Tipo de pedido (Local / Para llevar): ")
    
    try:
        # Convertimos los datos numéricos a sus tipos correspondientes
        total_pedido = float(input("Total del pedido: "))
        usuario_id = int(input("ID del Usuario que registra (ej. 1): "))
        
        # Lógica para la mesa: si es para llevar, la mesa queda como nula (None)
        if tipo_pedido.lower() == "local":
            mesa_id = int(input("ID de la Mesa (ej. 1, 2, 3): "))
        else:
            mesa_id = None
            
        estado_pedido = int(input("ID del Estado del Pedido (ej. 1 para Recibido): "))
        
    except ValueError:
        print("Error: Debes ingresar numeros validos para el total y los IDs.")
        return # Salimos de la función si el usuario escribe letras en lugar de números

    cursor = conexion.cursor()
    
    sql = """
    INSERT INTO PedidoVenta 
    (fechaPedido, tipoPedido, totalPedido, Usuario_idUsuario, Mesa_idMesa, EstadoPedido_idEstado) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    valores = (fecha_pedido, tipo_pedido, total_pedido, usuario_id, mesa_id, estado_pedido)
    
    try:
        cursor.execute(sql, valores)
        # Confirmamos la transacción
        conexion.commit()
        print(f"\nExito! Pedido guardado en la base de datos.")
        
    except Exception as e:
        print(f"\nError al guardar el pedido en la base de datos: {e}")
        # Deshacemos cualquier cambio en caso de error
        conexion.rollback()
        
    finally:
        # Solo cerramos el cursor, la conexión se mantiene abierta para el menú principal
        cursor.close()