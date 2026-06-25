import os
import mysql.connector
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )

        print("Conexion a la base de datos exitosa")
        return conexion
    
    except Exception as e:
        print("Error al conectar a la base de datos")
        print(e)
        return None
# ... (todo tu código anterior)

# LLAMADA A LA FUNCIÓN
if __name__ == "__main__":
    conectar()