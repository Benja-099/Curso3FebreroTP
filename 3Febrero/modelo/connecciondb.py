import sqlite3
import os

class Conneccion:
    def __init__(self):
        self.base_datos = os.path.abspath('ddbb/peliculas.db')
        if not os.path.exists(self.base_datos):
            print(f"El archivo de la base de datos '{self.base_datos}' no existe.")
        try:
            self.conexion = sqlite3.connect(self.base_datos)
            self.cursor = self.conexion.cursor()
            print(f"Conexión a la base de datos '{self.base_datos}' establecida correctamente.")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar_con(self):
        try:
            self.conexion.commit()
            self.conexion.close()
            print("Conexión cerrada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")