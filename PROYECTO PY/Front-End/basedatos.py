import mysql.connector

def conectar():
    """Crea la conexión a la base de datos JIO."""
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="ISRAEL123",
        database="JIO"  # 👈 agrega esto
    )
    return conexion

def crear_base_y_tablas():
    """Crea la base de datos y tablas si no existen."""
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="ISRAEL123"
    )
    cursor = conexion.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS JIO")
    cursor.execute("USE JIO")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id_categoria INT AUTO_INCREMENT PRIMARY KEY,
            nombre_categoria VARCHAR(50) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS producto (
            id_producto INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
            stock INT NOT NULL CHECK (stock >= 0),
            id_categoria INT,
            FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        )
    """)

    conexion.commit()
    conexion.close()

# Solo se ejecuta si se corre directamente
if __name__ == "__main__":
    crear_base_y_tablas()
    print("Base de datos y tablas listas.")
