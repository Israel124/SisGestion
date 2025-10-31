import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """ """
    try:
        conexion = mysql.connector.connect(
            host='localhost',      # Servidor MySQL
            user='root',           # Usuario MySQL
            password='',           # Contraseña (ajústala si es necesaria)
            database='VentaJIO_db' # Nombre de la base de datos  /// Recueden que en este caso la BD debe exister en el servidor
        )
        if conexion.is_connected():
            print("Conexión establecida con MySQL")
            return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        return None
    
def crear_tablas(conexion):
    """
    Crea las tablas Categorias, Productos y salidasproducto si no existen.
    """
    try:
        cursor = conexion.cursor()

        # Tabla Categorias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categorias (
                IDCategoria INT AUTO_INCREMENT PRIMARY KEY,
                NombreCategoria VARCHAR(50) NOT NULL
                Descripcion  VARCHAR(70) NOT NULL
            );
        """)

        # Tabla Productos
        cursor.execute("""
            CREATE TABLE Productos (
                IDProducto INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(100) NOT NULL,
                Precio DECIMAL(10,2) NOT NULL,
                Stock INT NOT NULL,
                IDCategoria INT,
                FOREIGN KEY (IDCategoria) REFERENCES Categorias(IDCategoria)
            );
        """)

        # Tabla Salidasproductos
        cursor.execute("""
            CREATE TABLE Salidasproductos (
                IDSalida INT AUTO_INCREMENT PRIMARY KEY,
                IDProducto INT NOT NULL,
                Cantidad INT NOT NULL,
                Fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (IDroducto) REFERENCES Productos(IDProducto)
           );
        """)

        # Tabla Usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
                NombreUsuario VARCHAR(50) NOT NULL,
                Contrasena VARCHAR(255) NOT NULL,
                Rol VARCHAR(20) NOT NULL
            );
        """)

        # Confirmar cambios en la base de datos
        conexion.commit()
        print("Tablas creadas correctamente en MySQL")

    except Error as e:
        print(f"Error al crear tablas: {e}")
