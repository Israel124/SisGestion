from tkinter import messagebox

def verificar_campos(txt_Producto, txt_Precio, txt_Stock, combo_categoria):
    producto = txt_Producto.get().strip()
    precio = txt_Precio.get().strip()
    stock = txt_Stock.get().strip()
    categoria = combo_categoria.get()

    # Validar que no estén vacíos
    if not producto or not precio or not stock or categoria == "Ninguno":
        messagebox.showerror("Error", "NO SE PUEDE DEJAR CAMPOS VACIOS Y DEBE TENER CATEGORIA")
        return False
    # Validar que producto solo tenga letras
    if not producto.replace(" ", "").isalpha():
        messagebox.showerror("Error", "El nombre del producto solo debe contener letras")
        return False
    # Validar que precio sea un número flotante válido
    try:
        precio_float = float(precio)
        if precio_float < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un número válido y positivo")
        return False
    # Validar que stock sea un número entero
    if not stock.isdigit():
        messagebox.showerror("Error", "El stock debe ser un número entero")
        return False

    return True
