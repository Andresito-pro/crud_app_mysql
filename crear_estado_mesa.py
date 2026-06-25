from conexion import conectar

def crear_tabla_estado_mesa():
    conexion = conectar()
    
    if conexion:
        cursor = conexion.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS EstadoMesa (
            idEstadoMesa INT NOT NULL,
            nombreEstadoMs VARCHAR(45) NOT NULL,
            descripcionEstadoMs VARCHAR(45) NOT NULL,
            activoEstadoMs TINYINT NOT NULL,
            PRIMARY KEY (idEstadoMesa)
        ) ENGINE = InnoDB;
        """
        
        try:
            cursor.execute(sql)
            print("Tabla 'EstadoMesa' creada correctamente (o ya existia).")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()
            print("Conexion cerrada.")

if __name__ == "__main__":
    crear_tabla_estado_mesa()