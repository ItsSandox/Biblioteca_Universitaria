import customtkinter as tk
from tkinter import *


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Iniciar sesión')
        #self.iconbitmap('img\ini_sec.ico')
        self.geometry("1220x780")
        self.config(bg='#124E78')
        self.resizable(0, 0)
        self.frame = Frame(master = self, bg_color='#001220', fg_color='#001220', width=540, height=500)
        self.frame.place(x=0, y=0)


class Frame(tk.CTkFrame):
        def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         
         self.boton1 = tk.CTkButton(self, text= "Hola Mundo", height=20, width= 30)
         self.boton1.place(x=200, y=250)

         self.boton2 = tk.CTkButton(self, text= "Adios Mundo", height=20, width= 30)
         self.boton2.place(x=200, y=270)

         self.titulo = tk.CTkLabel(self, text= "TITULO", fg_color= "transparent")
         self.titulo.place(x=10, y=10)


    