from conexion import conectar

def insertar_mesa():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        
        mesa_data = [
            (1, 101, 1), 
            (2, 102, 2), 
            (3, 103, 1)  
        ]
        
        sql = "INSERT INTO Mesa (idMesa, numeroMesa, EstadoMesa_idEstadoMesa) VALUES (%s, %s, %s)"
        
        try:
            for mesa in mesa_data:
                cursor.execute(sql, mesa)
                print(f"Mesa numero '{mesa[1]}' preparada para insertar.")
            
            # Confirmamos los cambios en la base de datos
            conexion.commit()
            print("Exito! Todas las mesas fueron guardadas en la base de datos.")
            
        except Exception as e:
            print(f"Error al insertar los datos: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_mesa()