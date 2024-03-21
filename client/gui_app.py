import customtkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter as tkinter
from model.app_dao import insertar_registro, consulta_cedula
import datetime

fuente1 = ('Montserrat', 25,'normal')
fuente2 = ('Montserrat', 50,'normal')
class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Iniciar sesión')
        #self.iconbitmap('img\ini_sec.ico')
        self.geometry("1220x780")
        #self.config(bg='#212325')
        self.resizable(0, 0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.framemain = FrameRegistro(master = self)
        self.framemain.grid(row=0, column=0, padx=50, pady=50, sticky="nswe")
         
class FrameRegistro(tk.CTkFrame):
        def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         #def registro():
             #insertar_registro()
         
         def registrarse():
            nombre = self.nombre.get()
            apellido = self.apellido.get()
            sexo_valor = sexo.get()
            cedula = self.cedula.get()
            ocupacion_valor = ocupacion.get()
            fecha_hora_actual = datetime.datetime.now()
            fecha_hora_actual_str = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')
            if nombre != '' and apellido != '' and cedula != '':
                sqlcedula = 'SELECT CEDULA FROM USUARIOS WHERE CEDULA = ?'
                if consulta_cedula(sqlcedula, cedula) is not None:
                    messagebox.showerror('Error', 'Esa cedula ya esta registrada')
                else:
                    sql = "INSERT INTO USUARIOS(NOMBRE,APELLIDO,SEXO,CEDULA,FECHA_CREACION,OCUPACION) VALUES (?,?,?,?,GETDATE(),?)"
                    insertar_registro(sql, nombre, apellido, sexo_valor, cedula, ocupacion_valor)
                    messagebox.showinfo("Exito", "Cuenta creada")
            else:
                messagebox.showerror('Error','No dejar ningún campo vacío')
            
            
         sexo = tkinter.IntVar(value=3)
         ocupacion = tkinter.IntVar(value=3)

         self.titulo = tk.CTkLabel(self, text="Biblioteca", font= fuente2)
         self.titulo.grid(row=0, column=0, columnspan=2, padx=100, pady=(100,10))

         self.nombre = tk.CTkEntry(self, placeholder_text="Nombre", font= fuente1, width=900)
         self.nombre.grid(row=1, column=0, columnspan=2, padx=100, pady=10, sticky="nswe")

         self.apellido = tk.CTkEntry(self, placeholder_text="Apellido", font= fuente1)
         self.apellido.grid(row=2, column=0, columnspan=2, padx=100, pady=(10, 10), sticky="nswe")

         self.cedula = tk.CTkEntry(self, placeholder_text="Cedula", font= fuente1)
         self.cedula.grid(row=3, column=0, padx=100, columnspan=2, pady=(10, 10), sticky="nswe")

         self.sexom = tk.CTkRadioButton(self, text="Masculino", variable=sexo, value=0, font= fuente1)
         self.sexom.grid(row=4, column=0, padx=100, pady=(10,10), sticky="nswe")

         self.sexof = tk.CTkRadioButton(self, text="Femenino", variable=sexo, value=1, font= fuente1)
         self.sexof.grid(row=4, column=1, padx=100, pady=(10,10), sticky="nswe")

         self.ocupacionE = tk.CTkRadioButton(self, text="Estudiante", variable=ocupacion, value=0, font= fuente1)
         self.ocupacionE.grid(row=5, column=0, padx=100, pady=(10,10), sticky="nswe")

         self.ocupacionP = tk.CTkRadioButton(self, text="Profesor", variable=ocupacion, value=1, font= fuente1)
         self.ocupacionP.grid(row=5, column=1, padx=100, pady=(10,10), sticky="nswe")

         self.registrarse = tk.CTkButton(self, text="Registrate", font= fuente1, command=registrarse)
         self.registrarse.grid(row=6, column=0, padx=100, pady=(10,10), sticky="we")
         


    