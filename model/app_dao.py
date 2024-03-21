from .conexion_db import conexionDB

def consulta_cedula(sql, cedula):
    conexion = conexionDB()
    conexion.cursor.execute(sql, [cedula])
    return conexion.cursor.fetchone()

def insertar_registro(sql, nombre, apellido, cedula, sexo, ocupacion):
    conexion = conexionDB()
    conexion.cursor.execute(sql, [nombre, apellido, cedula, sexo, ocupacion])
    conexion.conn.commit()