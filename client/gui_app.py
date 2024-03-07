import customtkinter as tk
from tkinter import *


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Iniciar sesión')
        #self.iconbitmap('img\ini_sec.ico')
        self.geometry("540x500")
        self.config(bg='#124E78')