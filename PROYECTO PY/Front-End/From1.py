import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class ProductManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("MICELANIA JIO - Sistema de Gestión")
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configura la ventana principal"""
        Wvent, Hvent = 900, 600
        anchopantalla = self.root.winfo_screenwidth()
        altopantalla = self.root.winfo_screenheight()
        x = (anchopantalla // 2) - (Wvent // 2)
        y = (altopantalla // 2) - (Hvent // 2)
        self.root.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
        self.root.resizable(False, False)
    
    def create_widgets(self):
        """Crea los widgets de la interfaz"""
        
        # Frame principal
        main_frame = tb.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)
        
        # Título
        title_label = tb.Label(
            main_frame, 
            text="Registro de Datos", 
            font=('Helvetica', 20, 'bold'),
            bootstyle=PRIMARY
        )
        title_label.pack(pady=(0, 20))
        
        # Frame para formulario de productos
        form_frame = tb.Frame(main_frame)
        form_frame.pack(fill=X, pady=(0, 10))
        
        # Fila 1 - Campos básicos
        row1 = tb.Frame(form_frame)
        row1.pack(fill=X, pady=5)
        
        # Nombre Producto
        tb.Label(row1, text="Nombre Producto:", bootstyle=PRIMARY).pack(side=LEFT, padx=5)
        self.txt_Producto = tb.Entry(row1, width=20)
        self.txt_Producto.pack(side=LEFT, padx=5)
        
        # Precio
        tb.Label(row1, text="Precio:", bootstyle=PRIMARY).pack(side=LEFT, padx=(20, 5))
        self.txt_Precio = tb.Entry(row1, width=15)
        self.txt_Precio.pack(side=LEFT, padx=5)
        
        # Stock
        tb.Label(row1, text="Stock:", bootstyle=PRIMARY).pack(side=LEFT, padx=(20, 5))
        self.txt_Stock = tb.Entry(row1, width=15)
        self.txt_Stock.pack(side=LEFT, padx=5)
        
        # Fila 2 - Categoría
        row2 = tb.Frame(form_frame)
        row2.pack(fill=X, pady=10)
        
        tb.Label(row2, text="Seleccione una Categoria", bootstyle=PRIMARY).pack(side=LEFT, padx=5)
        self.combo_categoria = ttk.Combobox(
            row2,
            values=["Alimentos", "Bebidas", "Snacks y Golosinas", "Limpieza", "Higiene Personal"],
            state="readonly",
            width=32
        )
        self.combo_categoria.pack(side=LEFT, padx=10)
        self.combo_categoria.set("Ninguno")
        
        # Frame CRUD
        frame_crud = tb.LabelFrame(
            form_frame,
            text="CRUD",
            bootstyle=PRIMARY,
            padding=10
        )
        frame_crud.pack(fill=X, pady=10)
        
        # Botones CRUD
        btn_frame = tb.Frame(frame_crud)
        btn_frame.pack()
        
        self.btn_Crear = tb.Button(
            btn_frame, 
            text="Crear", 
            bootstyle=SUCCESS,
            width=10
        )
        self.btn_Crear.pack(side=LEFT, padx=5)
        
        self.btn_Leer = tb.Button(
            btn_frame, 
            text="Leer", 
            bootstyle=INFO,
            width=10
        )
        self.btn_Leer.pack(side=LEFT, padx=5)
        
        self.btn_Actualizar = tb.Button(
            btn_frame, 
            text="Actualizar", 
            bootstyle=WARNING,
            width=10
        )
        self.btn_Actualizar.pack(side=LEFT, padx=5)
        
        self.btn_Borrar = tb.Button(
            btn_frame, 
            text="Borrar", 
            bootstyle=DANGER,
            width=10
        )
        self.btn_Borrar.pack(side=LEFT, padx=5)
        
        # Frame para tabla y opciones
        content_frame = tb.Frame(main_frame)
        content_frame.pack(fill=BOTH, expand=True)
        
        # Frame para tabla
        table_frame = tb.Frame(content_frame)
        table_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Tabla de productos
        columns = ("Nombre", "Precio", "Stock", "Categoria")
        self.tabla = ttk.Treeview(
            table_frame, 
            columns=columns, 
            show='headings',
            height=15
        )
        
        # Configurar columnas
        for col in columns:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=130, anchor="center")
        
        # Scrollbar para tabla
        scrollbar = tb.Scrollbar(table_frame, orient=VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Frame para opciones
        options_frame = tb.LabelFrame(
            content_frame,
            text="OPCIONES",
            bootstyle=PRIMARY,
            padding=10,
            width=120
        )
        options_frame.pack(side=RIGHT, fill=Y, padx=(10, 0))
        options_frame.pack_propagate(False)
        
        # Botones de opciones
        self.btn_LimitStock = tb.Button(
            options_frame,
            text="Limit Stock",
            bootstyle=WARNING,
            width=12
        )
        self.btn_LimitStock.pack(pady=5)
        
        self.btn_SalidaProd = tb.Button(
            options_frame,
            text="Salida Prod",
            bootstyle=INFO,
            width=12
        )
        self.btn_SalidaProd.pack(pady=5)
        
        self.btn_Salida = tb.Button(
            options_frame,
            text="Salida",
            command=self.cerrar,
            bootstyle=DANGER,
            width=12
        )
        self.btn_Salida.pack(pady=5)
        
        # Configurar eventos
        self.setup_events()
    
    def setup_events(self):
        """Configura los eventos de los botones"""
        self.tabla.bind('<<TreeviewSelect>>', self.on_product_select)
    
    def on_product_select(self, event):
        """Cuando se selecciona un producto en la tabla"""
        selected = self.tabla.selection()
        if selected:
            item = self.tabla.item(selected[0])
            values = item['values']
            
            # Llenar formulario con datos seleccionados
            self.txt_Producto.delete(0, tk.END)
            self.txt_Precio.delete(0, tk.END)
            self.txt_Stock.delete(0, tk.END)
            
            if values:
                self.txt_Producto.insert(0, values[0] if len(values) > 0 else "")
                self.txt_Precio.insert(0, values[1] if len(values) > 1 else "")
                self.txt_Stock.insert(0, values[2] if len(values) > 2 else "")
                if len(values) > 3:
                    self.combo_categoria.set(values[3])
    
    def clear_form(self):
        """Limpia el formulario"""
        self.txt_Producto.delete(0, tk.END)
        self.txt_Precio.delete(0, tk.END)
        self.txt_Stock.delete(0, tk.END)
        self.combo_categoria.set("Ninguno")
        # Limpiar selección de la tabla
        for item in self.tabla.selection():
            self.tabla.selection_remove(item)
    
    def cerrar(self):
        """Cierra la aplicación"""
        if messagebox.askokcancel("Salir", "¿Está seguro de que desea salir?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    
    root.style = tb.Style(theme="cyborg")
    
    app = ProductManagementSystem(root)
    root.mainloop()