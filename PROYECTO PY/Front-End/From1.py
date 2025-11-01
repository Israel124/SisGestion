import tkinter as tk
from tkinter import messagebox, ttk
from basedatos import crear_base_y_tablas
from LimitStock import abrir_Limit
from CRUD import agregar_producto, obtener_productos, agregar_categoria, obtener_categorias, eliminar_producto, actualizar_producto, obtener_productos_por_categoria

class ModernApp:
    def __init__(self):
        # --- Crear la base y tablas al iniciar ---
        crear_base_y_tablas()

        # --- Asegurar categorías iniciales ---
        if not obtener_categorias():
            categorias_iniciales = ["Alimentos", "Bebidas", "Snacks y Golosinas", "Limpieza", "Higiene Personal"]
            for cat in categorias_iniciales:
                agregar_categoria(cat)

        self.ventana = tk.Tk()
        self.ventana.title("MICELANIA JIO - Sistema de Gestión")
        self.setup_window()
        self.create_widgets()
        self.actualizar_tabla()

    def setup_window(self):
        """Configura la ventana con estilo Cyborg (oscuro)"""
        Wvent, Hvent = 1200, 700
        x = (self.ventana.winfo_screenwidth() // 2) - (Wvent // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (Hvent // 2)
        self.ventana.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
        self.ventana.resizable(True, True)
        
        # Colores estilo Cyborg
        self.bg_dark = "#2A2A2E"
        self.bg_card = "#3A3A3E"
        self.bg_darker = "#1A1A1E"
        self.primary = "#00A8FF"
        self.success = "#00D2A0"
        self.warning = "#FF9F1C"
        self.danger = "#FF6B6B"
        self.info = "#9B59B6"
        self.text_light = "#FFFFFF"
        self.text_muted = "#B0B0B0"
        
        self.ventana.configure(bg=self.bg_dark)

    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.ventana, bg=self.bg_dark, padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header con título
        header_frame = tk.Frame(main_frame, bg=self.bg_darker, pady=12, padx=15)
        header_frame.pack(fill=tk.X, pady=(0, 15))

        title_label = tk.Label(
            header_frame,
            text="🛍️ MICELANIA JIO - Sistema de Gestión de Productos",
            font=("Arial", 14, "bold"),
            bg=self.bg_darker,
            fg=self.primary
        )
        title_label.pack(side=tk.LEFT)

        # Filtros rápidos en el header
        filter_frame = tk.Frame(header_frame, bg=self.bg_darker)
        filter_frame.pack(side=tk.RIGHT)

        self.create_small_button(filter_frame, "📋 Todos", self.mostrar_todos, self.primary).pack(side=tk.LEFT, padx=3)
        self.create_small_button(filter_frame, "⚠️ Stock Bajo", self.filtrar_stock_bajo, self.warning).pack(side=tk.LEFT, padx=3)
        self.create_small_button(filter_frame, "🧹 Limpiar", self.limpiar_filtros, self.info).pack(side=tk.LEFT, padx=3)

        # Contenedor principal
        content_frame = tk.Frame(main_frame, bg=self.bg_dark)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # --- LADO IZQUIERDO: Formulario y Controles ---
        left_frame = tk.Frame(content_frame, bg=self.bg_dark, width=380)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        left_frame.pack_propagate(False)

        # Container scrollable para el panel izquierdo
        left_canvas = tk.Canvas(left_frame, bg=self.bg_dark, highlightthickness=0)
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=left_canvas.yview)
        scrollable_frame = tk.Frame(left_canvas, bg=self.bg_dark)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        )

        left_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=360)
        left_canvas.configure(yscrollcommand=scrollbar.set)

        left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind mouse wheel
        left_canvas.bind("<MouseWheel>", lambda e: left_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # --- SECCIÓN 1: Formulario de Producto ---
        form_card = tk.Frame(scrollable_frame, bg=self.bg_card, padx=15, pady=15, relief="ridge", bd=1)
        form_card.pack(fill=tk.X, pady=(0, 10))

        tk.Label(form_card, text="📝 REGISTRO DE PRODUCTOS", bg=self.bg_card, fg=self.primary,
                font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 12))

        # Campos del formulario
        tk.Label(form_card, text="Nombre Producto:", bg=self.bg_card, fg=self.text_light, 
                font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 4))
        self.txt_Producto = self.create_modern_entry(form_card)
        self.txt_Producto.pack(fill=tk.X, pady=(0, 12))

        # Fila para Precio y Stock
        price_stock_frame = tk.Frame(form_card, bg=self.bg_card)
        price_stock_frame.pack(fill=tk.X, pady=(0, 12))

        # Precio
        price_frame = tk.Frame(price_stock_frame, bg=self.bg_card)
        price_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        tk.Label(price_frame, text="Precio ($):", bg=self.bg_card, fg=self.text_light, 
                font=("Arial", 9, "bold")).pack(anchor="w")
        self.txt_Precio = self.create_modern_entry(price_frame)
        self.txt_Precio.pack(fill=tk.X, pady=(4, 0))

        # Stock
        stock_frame = tk.Frame(price_stock_frame, bg=self.bg_card)
        stock_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(8, 0))
        tk.Label(stock_frame, text="Stock:", bg=self.bg_card, fg=self.text_light, 
                font=("Arial", 9, "bold")).pack(anchor="w")
        self.txt_Stock = self.create_modern_entry(stock_frame)
        self.txt_Stock.pack(fill=tk.X, pady=(4, 0))

        # Categoría
        tk.Label(form_card, text="Categoría:", bg=self.bg_card, fg=self.text_light, 
                font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 4))
        
        categorias = [cat[1] for cat in obtener_categorias()]
        self.combo_categoria = ttk.Combobox(
            form_card,
            values=categorias,
            state="readonly",
            font=("Arial", 9),
            height=8
        )
        self.combo_categoria.pack(fill=tk.X, pady=(0, 8))
        self.combo_categoria.set("Seleccionar categoría")

        # --- SECCIÓN 2: Botones CRUD ---
        crud_card = tk.Frame(scrollable_frame, bg=self.bg_card, padx=15, pady=15, relief="ridge", bd=1)
        crud_card.pack(fill=tk.X, pady=(0, 10))

        tk.Label(crud_card, text="🛠️ OPERACIONES CRUD", bg=self.bg_card, fg=self.primary,
                font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 12))

        # Botones CRUD en grid 2x2
        crud_grid = tk.Frame(crud_card, bg=self.bg_card)
        crud_grid.pack(fill=tk.X)

        self.btn_crear = self.create_crud_button(crud_grid, "➕ CREAR", self.crear_producto, self.success)
        self.btn_crear.grid(row=0, column=0, sticky="ew", padx=3, pady=3)
        
        self.btn_actualizar = self.create_crud_button(crud_grid, "✏️ ACTUALIZAR", self.modificar_producto, self.warning)
        self.btn_actualizar.grid(row=0, column=1, sticky="ew", padx=3, pady=3)
        
        self.btn_leer = self.create_crud_button(crud_grid, "👁️ LEER TODO", self.actualizar_tabla, self.primary)
        self.btn_leer.grid(row=1, column=0, sticky="ew", padx=3, pady=3)
        
        self.btn_borrar = self.create_crud_button(crud_grid, "🗑️ ELIMINAR", self.borrar_producto, self.danger)
        self.btn_borrar.grid(row=1, column=1, sticky="ew", padx=3, pady=3)

        crud_grid.columnconfigure(0, weight=1)
        crud_grid.columnconfigure(1, weight=1)

        # --- SECCIÓN 3: Filtros Avanzados ---
        filter_card = tk.Frame(scrollable_frame, bg=self.bg_card, padx=15, pady=15, relief="ridge", bd=1)
        filter_card.pack(fill=tk.X, pady=(0, 10))

        tk.Label(filter_card, text="🔍 FILTROS AVANZADOS", bg=self.bg_card, fg=self.primary,
                font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 12))

        # Filtro por categoría
        tk.Label(filter_card, text="Filtrar por categoría:", bg=self.bg_card, fg=self.text_light,
                font=("Arial", 9)).pack(anchor="w", pady=(0, 4))
        
        self.combo_filtro_categoria = ttk.Combobox(
            filter_card,
            values=["Todas"] + categorias,
            state="readonly",
            font=("Arial", 9),
            height=8
        )
        self.combo_filtro_categoria.pack(fill=tk.X, pady=(0, 10))
        self.combo_filtro_categoria.set("Todas")
        self.combo_filtro_categoria.bind('<<ComboboxSelected>>', self.aplicar_filtros)

        # Filtro por stock
        tk.Label(filter_card, text="Filtrar por stock:", bg=self.bg_card, fg=self.text_light,
                font=("Arial", 9)).pack(anchor="w", pady=(0, 4))
        
        stock_filter_frame = tk.Frame(filter_card, bg=self.bg_card)
        stock_filter_frame.pack(fill=tk.X, pady=(0, 8))
        
        self.var_stock_filter = tk.StringVar(value="Todos")
        filters = [
            ("Todos", "Todos"),
            ("Stock Bajo (<10)", "Bajo"),
            ("Sin Stock", "Sin")
        ]
        
        for text, value in filters:
            tk.Radiobutton(stock_filter_frame, text=text, variable=self.var_stock_filter,
                          value=value, command=self.aplicar_filtros, bg=self.bg_card, 
                          fg=self.text_light, selectcolor=self.bg_darker,
                          font=("Arial", 8)).pack(side=tk.LEFT, padx=(0, 10))

        # --- SECCIÓN 4: Otras Opciones ---
        options_card = tk.Frame(scrollable_frame, bg=self.bg_card, padx=15, pady=15, relief="ridge", bd=1)
        options_card.pack(fill=tk.X)

        tk.Label(options_card, text="⚙️ OTRAS OPCIONES", bg=self.bg_card, fg=self.primary,
                font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 12))

        options = [
            ("⚠️ LÍMITE DE STOCK", abrir_Limit, self.warning),
            ("🧹 LIMPIAR FORMULARIO", self.limpiar_campos, self.info),
            ("🚪 SALIR DEL SISTEMA", self.cerrar, self.danger)
        ]

        for text, command, color in options:
            btn = self.create_option_button(options_card, text, command, color)
            btn.pack(fill=tk.X, pady=4)

        # --- LADO DERECHO: Tabla ---
        right_frame = tk.Frame(content_frame, bg=self.bg_dark)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Card de la tabla
        table_card = tk.Frame(right_frame, bg=self.bg_card, padx=15, pady=15, relief="ridge", bd=1)
        table_card.pack(fill=tk.BOTH, expand=True)

        # Header de la tabla con contador
        table_header = tk.Frame(table_card, bg=self.bg_card)
        table_header.pack(fill=tk.X, pady=(0, 12))

        tk.Label(table_header, text="📦 LISTA DE PRODUCTOS", bg=self.bg_card, fg=self.primary,
                font=("Arial", 11, "bold")).pack(side=tk.LEFT)

        self.lbl_contador = tk.Label(table_header, text="(0 productos)", bg=self.bg_card, fg=self.text_muted,
                                   font=("Arial", 9))
        self.lbl_contador.pack(side=tk.RIGHT)

        # Crear tabla
        self.create_table(table_card)

    def create_table(self, parent):
        """Crea y configura la tabla de productos"""
        # Frame para tabla y scrollbar
        table_frame = tk.Frame(parent, bg=self.bg_card)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self.tabla = ttk.Treeview(
            table_frame, 
            columns=("ID", "Nombre", "Precio", "Stock", "Categoria"), 
            show="headings",
            height=18
        )

        # Configurar estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview", 
                       background=self.bg_darker,
                       foreground=self.text_light,
                       fieldbackground=self.bg_darker,
                       borderwidth=0,
                       font=("Arial", 9))
        style.configure("Treeview.Heading",
                       background=self.primary,
                       foreground=self.text_light,
                       borderwidth=0,
                       font=("Arial", 9, "bold"))
        style.map("Treeview.Heading", background=[('active', '#0097E6')])

        # Configurar columnas
        column_config = [
            ("ID", 50), ("Nombre", 200), ("Precio", 80), 
            ("Stock", 60), ("Categoria", 120)
        ]
        
        for col, width in column_config:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=width, anchor="center")

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Grid para tabla y scrollbars
        self.tabla.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        # Bind eventos
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_producto)

    def create_modern_entry(self, parent):
        """Crea un campo de entrada moderno"""
        return tk.Entry(parent, font=("Arial", 10), bg=self.bg_darker, 
                      fg=self.text_light, insertbackground=self.text_light,
                      relief="flat", bd=0, highlightthickness=1, 
                      highlightbackground=self.primary, highlightcolor=self.primary)

    def create_crud_button(self, parent, text, command, color):
        """Crea un botón CRUD"""
        return self.create_button(parent, text, command, color, padding=8)

    def create_option_button(self, parent, text, command, color):
        """Crea un botón de opciones"""
        return self.create_button(parent, text, command, color, padding=10)

    def create_small_button(self, parent, text, command, color):
        """Crea un botón pequeño"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=self.text_light,
            font=("Arial", 8, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=5,
            cursor="hand2"
        )
        
        def on_enter(e):
            btn['bg'] = self.darken_color(color)
        def on_leave(e):
            btn['bg'] = color
            
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    def create_button(self, parent, text, command, color, padding=10):
        """Crea un botón con estilo moderno"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=self.text_light,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=padding,
            pady=padding,
            cursor="hand2"
        )
        
        def on_enter(e):
            btn['bg'] = self.darken_color(color)
        def on_leave(e):
            btn['bg'] = color
            
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    def darken_color(self, color):
        """Oscurece un color hexadecimal"""
        rgb = [int(color[i:i+2], 16) for i in (1, 3, 5)]
        darkened = [max(0, c - 30) for c in rgb]
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"

    # --- Funciones CRUD y Filtros ---
    def actualizar_tabla(self, productos=None):
        """Actualiza la tabla con los productos"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        if productos is None:
            productos = obtener_productos()

        # Aplicar filtros
        categoria_filtro = self.combo_filtro_categoria.get()
        if categoria_filtro != "Todas":
            productos = [p for p in productos if p[4] == categoria_filtro]

        stock_filter = self.var_stock_filter.get()
        if stock_filter != "Todos":
            if stock_filter == "Bajo":
                productos = [p for p in productos if p[3] < 10]
            elif stock_filter == "Sin":
                productos = [p for p in productos if p[3] == 0]

        for p in productos:
            self.tabla.insert("", "end", values=p)

        # Actualizar contador
        self.lbl_contador.config(text=f"({len(productos)} productos)")

    def aplicar_filtros(self, event=None):
        """Aplica los filtros seleccionados"""
        self.actualizar_tabla()

    def mostrar_todos(self):
        """Muestra todos los productos"""
        self.combo_filtro_categoria.set("Todas")
        self.var_stock_filter.set("Todos")
        self.actualizar_tabla()

    def filtrar_stock_bajo(self):
        """Filtra productos con stock bajo"""
        self.var_stock_filter.set("Bajo")
        self.actualizar_tabla()

    def limpiar_filtros(self):
        """Limpia todos los filtros"""
        self.mostrar_todos()

    def crear_producto(self):
        try:
            nombre = self.txt_Producto.get()
            precio = float(self.txt_Precio.get())
            stock = int(self.txt_Stock.get())
            
            categoria_nombre = self.combo_categoria.get()
            if nombre == "" or categoria_nombre == "Seleccionar categoría":
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return

            # Obtener ID de la categoría
            categorias = obtener_categorias()
            id_categoria = None
            for cat in categorias:
                if cat[1] == categoria_nombre:
                    id_categoria = cat[0]
                    break

            if id_categoria is None:
                messagebox.showerror("Error", "Categoría no válida.")
                return

            agregar_producto(nombre, precio, stock, id_categoria)
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
            self.actualizar_tabla()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Precio y Stock deben ser números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el producto.\n{str(e)}")

    def borrar_producto(self):
        seleccionado = self.tabla.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto para eliminar.")
            return
        valores = self.tabla.item(seleccionado, "values")
        id_producto = valores[0]
        eliminar_producto(id_producto)
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        self.actualizar_tabla()
        self.limpiar_campos()

    def modificar_producto(self):
        seleccionado = self.tabla.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto para actualizar.")
            return
        valores = self.tabla.item(seleccionado, "values")
        id_producto = valores[0]
        try:
            nombre = self.txt_Producto.get()
            precio = float(self.txt_Precio.get())
            stock = int(self.txt_Stock.get())
            
            categoria_nombre = self.combo_categoria.get()
            if nombre == "" or categoria_nombre == "Seleccionar categoría":
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return

            # Obtener ID de la categoría
            categorias = obtener_categorias()
            id_categoria = None
            for cat in categorias:
                if cat[1] == categoria_nombre:
                    id_categoria = cat[0]
                    break

            if id_categoria is None:
                messagebox.showerror("Error", "Categoría no válida.")
                return

            actualizar_producto(id_producto, nombre, precio, stock, id_categoria)
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.actualizar_tabla()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Precio y Stock deben ser números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el producto.\n{str(e)}")

    def limpiar_campos(self):
        self.txt_Producto.delete(0, tk.END)
        self.txt_Precio.delete(0, tk.END)
        self.txt_Stock.delete(0, tk.END)
        self.combo_categoria.set("Seleccionar categoría")

    def seleccionar_producto(self, event):
        seleccionado = self.tabla.focus()
        if not seleccionado:
            return
        valores = self.tabla.item(seleccionado, "values")
        self.txt_Producto.delete(0, tk.END)
        self.txt_Producto.insert(0, valores[1])
        self.txt_Precio.delete(0, tk.END)
        self.txt_Precio.insert(0, valores[2])
        self.txt_Stock.delete(0, tk.END)
        self.txt_Stock.insert(0, valores[3])
        self.combo_categoria.set(valores[4])

    def cerrar(self):
        if messagebox.askokcancel("Confirmación", "¿Seguro de querer salir?"):
            self.ventana.destroy()

    def run(self):
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.ventana.mainloop()

def menu():
    app = ModernApp()
    app.run()

if __name__ == "__main__":
    menu()