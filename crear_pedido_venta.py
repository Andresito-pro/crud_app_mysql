from conexion import conectar

def crear_tabla_pedido_venta():
    conexion = conectar()
    
    if conexion:
        cursor = conexion.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS PedidoVenta (
            idPedidoVenta INT NOT NULL AUTO_INCREMENT,
            fechaPedido DATETIME NOT NULL,
            tipoPedido VARCHAR(45) NOT NULL,
            totalPedido DECIMAL(10,2) NOT NULL,
            Usuario_idUsuario INT NOT NULL,
            Mesa_idMesa INT NULL,
            EstadoPedido_idEstado INT NOT NULL,
            PRIMARY KEY (idPedidoVenta),
            INDEX fk_PedidoVenta_Mesa1_idx (Mesa_idMesa),
            CONSTRAINT fk_PedidoVenta_Mesa1
                FOREIGN KEY (Mesa_idMesa)
                REFERENCES Mesa (idMesa)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE = InnoDB;
        """
        
        try:
            cursor.execute(sql)
            print("Tabla 'PedidoVenta' creada correctamente (o ya existia).")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()
            print("Conexion cerrada.")

if __name__ == "__main__":
    crear_tabla_pedido_venta()