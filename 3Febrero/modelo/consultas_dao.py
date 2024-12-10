from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Genero INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID)
        );
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


class Peliculas():

    def __init__(self,nombre,duracion,genero,clasificacion,calificacion):
       self.nombre = nombre
       self.duracion = duracion
       self.genero = genero
       self.clasificaion = clasificacion
       self.clasificaion = calificacion

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero},{self.clasificacion},{self.calificacion}]'

def guardar_peli(pelicula):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Peliculas(Nombre,Duracion,Genero)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},{pelicula.clasificacion},{pelicula.calificacion});
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql = '''
        SELECT Peliculas.ID,Clasificacion.nombreClasificacion, Peliculas.Nombre, Peliculas.Duracion, Genero.Nombre, Peliculas.calificacion from Peliculas	INNER JOIN Clasificacion on Peliculas.idClasificacion_p=Clasificacion.idClasificacion inner join Genero on Genero.ID=Peliculas.Genero;
    '''
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except Exception as e:
        print(f"Error al listar películas: {e}")
        return []


def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql = '''
        SELECT * FROM Genero;
    '''
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        print(f"Géneros obtenidos: {listar_genero}")  # Mensaje de depuración
        conn.cerrar_con()

        return listar_genero
    except Exception as e:
        print(f"Error al listar géneros: {e}")
        return []


def listar_Clasificacion():#---------------eto agrgegr
    conn = Conneccion()
    listar_clasi = []

    sql = '''
        SELECT * FROM Clasificacion ;
    '''
    try:
        conn.cursor.execute(sql)
        listar_clasi = conn.cursor.fetchall()
        print(f"Géneros obtenidos: {listar_clasi}")  
        conn.cerrar_con()

        return listar_clasi
    except Exception as e:
        print(f"Error al listar las clasificaciones: {e}")
        return []


def listar_calificacion():#---------------eto agrgegr
    conn = Conneccion()
    listar_clasi = []

    sql = '''
       SELECT* FROM calificacion;
    '''
    try:
        conn.cursor.execute(sql)
        listar_cali = conn.cursor.fetchall()
        print(f"Calificaion obtenidos: {listar_cali}")  
        conn.cerrar_con()

        return listar_cali
    except Exception as e:
        print(f"Error al listar las calificaiones: {e}")
        return []



def editar_peli(pelicula, id):
    conn = Conneccion()

    sql= f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}, Clasificacion = {pelicula.clasificacion}, Calificacion = {pelicula.calificaion}
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_peli(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Peliculas
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass



class Clasificacion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Clasificacion[{self.nombre}]'

def guardar_clasificacion(clasificacion):
    conn = Conneccion()

    sql = f'''
        INSERT INTO Clasificacion(nombreClasificacion)
        VALUES('{clasificacion.nombre}');
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar clasificación: {e}")

def listar_clasificaciones():
    conn = Conneccion()
    listar_clasificaciones = []

    sql = '''
        SELECT * FROM Clasificacion;
    '''
    try:
        conn.cursor.execute(sql)
        listar_clasificaciones = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_clasificaciones
    except Exception as e:
        print(f"Error al listar clasificaciones: {e}")
        return []

def buscar_clasificacion_por_nombre(nombre):
    conn = Conneccion()
    clasificaciones = []

    sql = "SELECT * FROM Clasificacion WHERE nombreClasificacion LIKE '%"+nombre+"%';"
   
    try:
        conn.cursor.execute(sql)
        clasificaciones = conn.cursor.fetchall()
        conn.cerrar_con()

        return clasificaciones
    except Exception as e:
        print(f"Error al buscar clasificación: {e}")
        return []