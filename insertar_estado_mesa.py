from conexion import conectar

def insertar_estado_mesa():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        
        estado_mesa_data = [
            (1, "Disponible", "Mesa libre y limpia", 1),
            (2, "Ocupada", "Mesa con clientes actuales", 1),
            (3, "Mantenimiento", "Mesa en reparacion", 0)
        ]
        
        sql = "INSERT INTO EstadoMesa (idEstadoMesa, nombreEstadoMs, descripcionEstadoMs, activoEstadoMs) VALUES (%s, %s, %s, %s)"
        
        try:
            for estado in estado_mesa_data:
                cursor.execute(sql, estado)
                print(f"Estado '{estado[1]}' preparado para insertar.")
            
            # Confirmamos los cambios en la base de datos
            conexion.commit()
            print("Exito! Todos los estados de mesa fueron guardados en la base de datos.")
            
        except Exception as e:
            print(f"Error al insertar los datos: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_estado_mesa()