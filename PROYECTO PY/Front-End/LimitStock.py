import tkinter as tk
from tkinter import messagebox #caja de texto
from tkinter import ttk

def abrir_Limit():
    ventana = tk.Tk()
    ventana.title("MICELANIA JIO")

    def cerrar():
            ventana.destroy()

    #CODIGO DE LA VENTANA
    Wvent = 300
    Hvent = 300
    anchopantalla = ventana.winfo_screenwidth()
    altopantalla = ventana.winfo_screenheight()
    x = (anchopantalla // 2) - (Wvent // 2)
    y = (altopantalla // 2) - (Hvent // 2)
    ventana.geometry(f"{Wvent}x{Hvent}+{x}+{y}")
    ventana.resizable(False,False)

    #LABES

    label_LimitStock = tk.Label(
        ventana,
        text="PRODUCTOS CON POCAS UNIDADES",
        font=("Arial", 10, "bold"),
        bg="#EDEDED",
        fg="#357AC5"  # color del texto
    )
    label_LimitStock.place(x=30, y=20)

    #GROUPBOX
    frame_Product = tk.LabelFrame(
        ventana,
        text="",   # título del grupo
        font=("Arial", 12, "bold"),
        bg="#D6EAF8",
        fg="#505559",
        padx=10,  # margen interno horizontal
        pady=10   # margen interno vertical
    )
    frame_Product.place(x=30, y=50, width=240, height=200)

    #BOTON
    btn_Cerrar = tk.Button(
        ventana,
        command=cerrar,
        text="    Cerrar    ",
        bg="#5DADE2",
        fg="white",
        activebackground="#3498DB",
        relief="ridge"
    )
    btn_Cerrar.place(x=110, y=260)
    ventana.mainloop()

