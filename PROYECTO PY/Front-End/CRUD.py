from basedatos import conectar

# ---------- CATEGORÍAS ----------
def agregar_categoria(nombre_categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categoria (nombre_categoria) VALUES (%s)", (nombre_categoria,))
    conexion.commit()
    conexion.close()

def obtener_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    datos = cursor.fetchall()
    conexion.close()
    return datos


# ---------- PRODUCTOS ----------
def agregar_producto(nombre, precio, stock, id_categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO producto (nombre, precio, stock, id_categoria)
        VALUES (%s, %s, %s, %s)
    """, (nombre, precio, stock, id_categoria))
    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre_categoria
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
    """)
    datos = cursor.fetchall()
    conexion.close()
    return datos

def actualizar_producto(id_producto, nombre, precio, stock, id_categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE producto
        SET nombre=%s, precio=%s, stock=%s, id_categoria=%s
        WHERE id_producto=%s
    """, (nombre, precio, stock, id_categoria, id_producto))
    conexion.commit()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto=%s", (id_producto,))
    conexion.commit()
    conexion.close()

def obtener_stock_bajo():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, stock FROM producto WHERE stock < 10")
    datos = cursor.fetchall()
    conexion.close()
    return datos

def obtener_productos_por_categoria(id_categoria=None):
    conexion = conectar()
    cursor = conexion.cursor()
    if id_categoria:
        cursor.execute("""
            SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre_categoria
            FROM producto p
            JOIN categoria c ON p.id_categoria = c.id_categoria
            WHERE p.id_categoria=%s
        """, (id_categoria,))
    else:
        cursor.execute("""
            SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre_categoria
            FROM producto p
            JOIN categoria c ON p.id_categoria = c.id_categoria
        """)
    datos = cursor.fetchall()
    conexion.close()
    return datos

