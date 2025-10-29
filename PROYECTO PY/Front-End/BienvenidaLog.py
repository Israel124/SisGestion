import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class BienvenidaLog:
    def __init__(self, root):
        self.root = root
        self.root.title("MISCELANEA JIO - Sistema de Gestión")
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configura la ventana principal"""
        Wvent, Hvent = 1000, 600
        anchopantalla = self.root.winfo_screenwidth()
        altopantalla = self.root.winfo_screenheight()
        x = (anchopantalla // 2) - (Wvent // 2)
        y = (altopantalla // 2) - (Hvent // 2)
        self.root.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
        self.root.resizable(False, False)
    
    def create_widgets(self):
        """Crea los widgets de la página de login"""
        
        # Frame principal con fondo oscuro
        main_frame = tb.Frame(self.root, padding=0)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # CONTENIDO PRINCIPAL - Dividido en dos secciones
        content_frame = tb.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # SECCIÓN IZQUIERDA - Logo e información
        left_frame = tb.Frame(content_frame, width=450)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 40))
        left_frame.pack_propagate(False)
        
        # Logo MISCELANEA JIO
        logo_frame = tb.Frame(left_frame)
        logo_frame.pack(anchor=tk.W, pady=(20, 30))
        
        # Logo principal
        logo_label = tb.Label(
            logo_frame,
            text="MISCELANEA\nJIO",
            font=('Arial', 28, 'bold'),
            bootstyle="primary",
            justify=tk.LEFT
        )
        logo_label.pack(side=tk.LEFT)
        
        # Mensaje de bienvenida
        welcome_frame = tb.Frame(left_frame)
        welcome_frame.pack(fill=tk.BOTH, expand=True, pady=40)
        
        welcome_title = tb.Label(
            welcome_frame,
            text="Bienvenido al Sistema",
            font=('Arial', 20, 'bold'),
            bootstyle="primary"
        )
        welcome_title.pack(anchor=tk.W, pady=(40, 15))
        
        welcome_text = tb.Label(
            welcome_frame,
            text="Sistema de Gestión de Inventario\n\n"
                 "Accede para gestionar productos, categorías\n"
                 "y controlar el stock de tu negocio.",
            font=('Arial', 12),
            bootstyle="secondary",
            justify=tk.LEFT
        )
        welcome_text.pack(anchor=tk.W)
        # SECCIÓN DERECHA - Formulario de login
        right_frame = tb.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Frame del formulario de login
        login_frame = tb.LabelFrame(
            right_frame,
            text=" Inicio de Sesión ",
            bootstyle="primary",
            padding=30
        )
        login_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título del formulario
        login_title = tb.Label(
            login_frame,
            text="Acceder al Sistema",
            font=('Arial', 18, 'bold'),
            bootstyle="primary"
        )
        login_title.pack(pady=(10, 40))
        
        # Campos del formulario
        # Usuario
        user_frame = tb.Frame(login_frame)
        user_frame.pack(fill=tk.X, pady=20)
        
        tb.Label(user_frame, text="Usuario:", 
                font=('Arial', 11, 'bold'), bootstyle="primary").pack(anchor=tk.W)
        self.username_entry = tb.Entry(user_frame, font=('Arial', 12), width=30)
        self.username_entry.pack(fill=tk.X, pady=(10, 0), ipady=8)
        
        # Contraseña
        pass_frame = tb.Frame(login_frame)
        pass_frame.pack(fill=tk.X, pady=20)
        
        tb.Label(pass_frame, text="Contraseña:", 
                font=('Arial', 11, 'bold'), bootstyle="primary").pack(anchor=tk.W)
        self.password_entry = tb.Entry(pass_frame, font=('Arial', 12), width=30, show="•")
        self.password_entry.pack(fill=tk.X, pady=(10, 0), ipady=8)
        
        # Botón de login (mejorado)
        btn_frame = tb.Frame(login_frame)
        btn_frame.pack(pady=40)
        
        login_btn = tb.Button(
            btn_frame,
            text="🚪 INICIAR SESIÓN",
            command=self.iniciar_sesion,
            bootstyle="success",
            width=25,
            padding=(15, 10)
        )
        login_btn.pack()
        
        # Enlaces de ayuda
        help_frame = tb.Frame(login_frame)
        help_frame.pack(pady=25)
        
        tb.Button(
            help_frame,
            text="¿Olvidaste tu contraseña?",
            command=self.recuperar_password,
            bootstyle="link-secondary"
        ).pack(side=tk.LEFT, padx=15)
        
        tb.Button(
            help_frame,
            text="Crear nueva cuenta",
            command=self.crear_cuenta,
            bootstyle="link-secondary"
        ).pack(side=tk.LEFT, padx=15)
        
        # Footer
        footer_frame = tb.Frame(main_frame, bootstyle="light")
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=15)
        
        footer = tb.Label(
            footer_frame,
            text="© 2024 MISCELANEA JIO - Sistema de Gestión v2.0",
            font=('Arial', 9),
            bootstyle="secondary"
        )
        footer.pack()
        
        # Bind Enter para facilitar el login
        self.password_entry.bind('<Return>', lambda e: self.iniciar_sesion())
        self.username_entry.focus()
    
    def iniciar_sesion(self):
        """Función para el botón iniciar sesión"""
        usuario = self.username_entry.get().strip()
        contraseña = self.password_entry.get().strip()
        
        if not usuario:
            messagebox.showwarning("Campo requerido", "Por favor ingresa tu usuario", parent=self.root)
            self.username_entry.focus()
            return
            
        if not contraseña:
            messagebox.showwarning("Campo requerido", "Por favor ingresa tu contraseña", parent=self.root)
            self.password_entry.focus()
            return
        
        # Simulación de login exitoso
        messagebox.showinfo(
            "Inicio de Sesión", 
            f"¡Bienvenido {usuario}!\n\nAccediendo al sistema de gestión...",
            parent=self.root
        )
        
        # Cerrar ventana de login
        self.root.destroy()
        
        # Aquí se abriría la ventana principal del sistema de productos
        # self.abrir_sistema_principal()
    
    def recuperar_password(self):
        messagebox.showinfo(
            "Recuperar Contraseña", 
            "Función disponible próximamente\nContacta al administrador del sistema",
            parent=self.root
        )
    
    def crear_cuenta(self):
        messagebox.showinfo(
            "Crear Cuenta", 
            "Función disponible próximamente\nContacta al administrador del sistema",
            parent=self.root
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.style = tb.Style(theme="cyborg")
    app = BienvenidaLog(root)
    root.mainloop()