from .conexion_db import conexionDB

def funcion():
    conectado = conexionDB()
    cursor = conectado.cursor()
