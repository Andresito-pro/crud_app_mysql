def ver_mesas(conexion):
    # Validamos que la conexión esté activa
    if not conexion:
        print("Error: No hay conexion a la base de datos.")
        return

    print("\n--- ESTADO DE LAS MESAS ---")
    cursor = conexion.cursor()
    
    # Hacemos un JOIN para unir la mesa con su estado
    sql = """
    SELECT m.numeroMesa, e.nombreEstadoMs, e.descripcionEstadoMs 
    FROM Mesa m
    INNER JOIN EstadoMesa e ON m.EstadoMesa_idEstadoMesa = e.idEstadoMesa
    """
    
    try:
        cursor.execute(sql)
        mesas = cursor.fetchall()
        
        if len(mesas) == 0:
            print("No hay mesas registradas.")
        else:
            print(f"{'Mesa':<10} | {'Estado':<15} | {'Descripcion'}")
            print("-" * 50)
            
            for m in mesas:
                print(f"{m[0]:<10} | {m[1]:<15} | {m[2]}")
                
    except Exception as e:
        print(f"Error al consultar las mesas: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()