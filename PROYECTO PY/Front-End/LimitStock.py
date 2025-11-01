import tkinter as tk
from tkinter import ttk
from CRUD import obtener_stock_bajo  # Importamos la función de stock bajo

def abrir_Limit():
    ventana = tk.Tk()
    ventana.title("MICELANIA JIO")

    # --- Función de cierre ---
    def cerrar():
        ventana.destroy()

    # --- Medidas de ventana ---
    Wvent, Hvent = 400, 350
    x = (ventana.winfo_screenwidth() // 2) - (Wvent // 2)
    y = (ventana.winfo_screenheight() // 2) - (Hvent // 2)
    ventana.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
    ventana.resizable(False, False)
    ventana.configure(bg="#EAF2F8")

    # --- Etiqueta ---
    tk.Label(
        ventana,
        text="PRODUCTOS CON POCAS UNIDADES (Stock < 10)",
        font=("Arial", 10, "bold"),
        bg="#EDEDED",
        fg="#357AC5"
    ).pack(pady=10)

    # --- Treeview para mostrar los productos ---
    tabla_stock = ttk.Treeview(ventana, columns=("Producto", "Stock"), show="headings", height=10)
    tabla_stock.heading("Producto", text="Producto")
    tabla_stock.heading("Stock", text="Stock")
    tabla_stock.column("Producto", width=200, anchor="center")
    tabla_stock.column("Stock", width=80, anchor="center")
    tabla_stock.pack(pady=10)

    # --- Función para cargar productos con stock bajo ---
    def cargar_stock_bajo():
        for fila in tabla_stock.get_children():
            tabla_stock.delete(fila)
        productos = obtener_stock_bajo()
        for p in productos:
            tabla_stock.insert("", "end", values=p)

    # --- Botón Cerrar ---
    tk.Button(
        ventana,
        text="Cerrar",
        bg="#5DADE2",
        fg="white",
        command=cerrar
    ).pack(pady=10)

    # --- Cargar datos al abrir la ventana ---
    cargar_stock_bajo()

    ventana.mainloop()
