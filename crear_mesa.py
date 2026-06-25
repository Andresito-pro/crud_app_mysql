from conexion import conectar

def crear_tabla_mesa():
    conexion = conectar()
    
    if conexion:
        cursor = conexion.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS Mesa (
            idMesa INT NOT NULL,
            numeroMesa INT NOT NULL,
            EstadoMesa_idEstadoMesa INT NOT NULL,
            PRIMARY KEY (idMesa),
            INDEX fk_Mesa_EstadoMesa1_idx (EstadoMesa_idEstadoMesa),
            CONSTRAINT fk_Mesa_EstadoMesa1
                FOREIGN KEY (EstadoMesa_idEstadoMesa)
                REFERENCES EstadoMesa (idEstadoMesa)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE = InnoDB;
        """
        
        try:
            cursor.execute(sql)
            print("Tabla 'Mesa' creada correctamente (o ya existia).")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()
            print("Conexion cerrada.")

if __name__ == "__main__":
    crear_tabla_mesa()