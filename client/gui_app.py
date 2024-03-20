import customtkinter as tk
from tkinter import *
fuente1 = ('Montserrat', 25,'normal')


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Iniciar sesión')
        #self.iconbitmap('img\ini_sec.ico')

        self.geometry("540x500")
        self.config(bg='#124E78')

        self.geometry("683x384")
        self.config(bg='#124E78')
        self.resizable(0, 0)
        self.frame = FrameReserva(master = self, bg_color='#001220', fg_color='#001220', width=683, height=384)
        self.frame.place(x=0, y=0)

class FrameReserva(tk.CTkFrame):
         
        def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)

         def guardar_datos():
                Cedula = self.cedula.get()
                Ojecto = self.Ojectivo.get()
                Fecha_entrega = self.Fecha_inicio.get()
                Fecha_salida = self.fecha_final.get()
                self.cursor.execute(f"insert into RESERVAS values ('{Cedula}','{Ojecto}','{Fecha_entrega}','{Fecha_salida}')")

         self.cedula = tk.CTkEntry(self,height=30, width= 300, placeholder_text="Cedula")
         self.cedula.place(x=200, y=50)

         self.Ojectivo = tk.CTkEntry(self,height=30, width= 300, placeholder_text="Libro o Aula")
         self.Ojectivo.place(x=200, y=100)

         self.Fecha_inicio = tk.CTkEntry(self,height=30, width= 300, placeholder_text="Hora a reservar")
         self.Fecha_inicio.place(x=200, y=150)

         self.fecha_final = tk.CTkEntry(self,height=30, width= 300, placeholder_text="Hora a Desreservar")
         self.fecha_final.place(x=200, y=200)
            
         self.ENTRE = tk.CTkButton(self, text= "➡️", fg_color= "transparent",command=guardar_datos)
         self.ENTRE.place(x=275, y=250)
         
