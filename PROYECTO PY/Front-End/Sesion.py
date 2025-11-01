import tkinter as tk
from tkinter import messagebox
from From1 import menu  # asegurate que menu sea una función o clase que abre la ventana

USUARIO_VALIDO = "es"
CONTRASENA_VALIDA = "123"

def validar_credenciales():
    UN = entry_usuario.get()
    contra = entry_contrasena.get()

    if UN == USUARIO_VALIDO and contra == CONTRASENA_VALIDA:
        messagebox.showinfo("Éxito", "¡Inicio de sesión correcto!")
        # Abrir el menu
        abrir_menu()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def abrir_menu():
    ventana.destroy()
    menu()

def on_enter_usuario(e):
    entry_usuario.config(bg="#F0F8FF", relief="solid")

def on_leave_usuario(e):
    entry_usuario.config(bg="white", relief="flat")

def on_enter_contrasena(e):
    entry_contrasena.config(bg="#F0F8FF", relief="solid")

def on_leave_contrasena(e):
    entry_contrasena.config(bg="white", relief="flat")

def on_enter_btn(e):
    btn_entrar.config(bg="#2980B9", relief="raised")

def on_leave_btn(e):
    btn_entrar.config(bg="#3498DB", relief="flat")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("MICELANIA JIO")
ventana.configure(bg="#2C3E50")

Wvent = 400
Hvent = 500
anchopantalla = ventana.winfo_screenwidth()
altopantalla = ventana.winfo_screenheight()
x = (anchopantalla // 2) - (Wvent // 2)
y = (altopantalla // 2) - (Hvent // 2)
ventana.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
ventana.resizable(False, False)

# Frame principal con sombra visual
frame_principal = tk.Frame(
    ventana,
    bg="#34495E",
    relief="raised",
    bd=0
)
frame_principal.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

# Título principal con estilo moderno
label_TituloSesion = tk.Label(
    frame_principal,
    text="MICELANIA JIO",
    font=("Arial", 24, "bold"),
    bg="#34495E",
    fg="#3498DB"
)
label_TituloSesion.place(relx=0.5, y=50, anchor="center")

# Subtítulo
label_subtitulo = tk.Label(
    frame_principal,
    text="Iniciar Sesión",
    font=("Arial", 12),
    bg="#34495E",
    fg="#BDC3C7"
)
label_subtitulo.place(relx=0.5, y=90, anchor="center")

# Usuario
label_NombreU = tk.Label(
    frame_principal,
    text="Usuario",
    font=("Arial", 10, "bold"),
    bg="#34495E",
    fg="#3498DB"
)
label_NombreU.place(x=50, y=140)

entry_usuario = tk.Entry(
    frame_principal,
    width=25,
    font=("Arial", 11),
    bg="white",
    fg="#2C3E50",
    relief="flat",
    bd=2
)
entry_usuario.place(x=50, y=165)
entry_usuario.bind("<FocusIn>", on_enter_usuario)
entry_usuario.bind("<FocusOut>", on_leave_usuario)

# Contraseña
label_contra = tk.Label(
    frame_principal,
    text="Contraseña",
    font=("Arial", 10, "bold"),
    bg="#34495E",
    fg="#3498DB"
)
label_contra.place(x=50, y=220)

entry_contrasena = tk.Entry(
    frame_principal,
    width=25,
    font=("Arial", 11),
    bg="white",
    fg="#2C3E50",
    relief="flat",
    bd=2,
    show="•"
)
entry_contrasena.place(x=50, y=245)
entry_contrasena.bind("<FocusIn>", on_enter_contrasena)
entry_contrasena.bind("<FocusOut>", on_leave_contrasena)

# Botón de login moderno
btn_entrar = tk.Button(
    frame_principal,
    text="INICIAR SESIÓN",
    command=validar_credenciales,
    font=("Arial", 12, "bold"),
    bg="#3498DB",
    fg="white",
    activebackground="#2980B9",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    width=20,
    height=2
)
btn_entrar.place(relx=0.5, y=350, anchor="center")
btn_entrar.bind("<Enter>", on_enter_btn)
btn_entrar.bind("<Leave>", on_leave_btn)

# Línea decorativa
linea_decorativa = tk.Frame(
    frame_principal,
    height=2,
    bg="#3498DB"
)
linea_decorativa.place(x=50, y=120, width=250)

# Información de credenciales (solo para desarrollo)
label_info = tk.Label(
    frame_principal,
    text="© 2025 MISCELANEA JIO - Sistema de Gestión v1.0",
    font=("Arial", 8),
    bg="#34495E",
    fg="#7F8C8D"
)
label_info.place(relx=0.5, y=400, anchor="center")

# Configurar el enfoque inicial
entry_usuario.focus_set()

# Permitir login con Enter
ventana.bind('<Return>', lambda event: validar_credenciales())

ventana.mainloop()