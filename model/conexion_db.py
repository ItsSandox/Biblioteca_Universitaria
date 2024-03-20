import pyodbc 

class conexionDB:
    def _init_(self):    
        try:
            server = "Laptop_Pikki"  
            database = "BIBLIOTECA"
            conexion = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};"

            # Conexion con libreria pyodbc
            conectado = pyodbc.connect(conexion)

            # Cursor para ejecutar consultas
            cursor = conectado.cursor()
            cursor_de_añadir = conectado.cursor()
            materia = conectado.cursor()
            print("Funciona la conecion")
        except:
            print("No funciona la conecion")