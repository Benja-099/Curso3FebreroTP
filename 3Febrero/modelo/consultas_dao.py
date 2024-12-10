from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql_genero = '''
        CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50)
        );
    '''
    sql_clasificacion = '''
        CREATE TABLE IF NOT EXISTS Clasificacion(
            idClasificacion INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreClasificacion VARCHAR(5) NOT NULL
        );
    '''
    sql_calificacion = '''
        CREATE TABLE IF NOT EXISTS Calificacion(
            idCalificacion INTEGER PRIMARY KEY AUTOINCREMENT,
            NumeroCalificacion INTEGER NOT NULL
        );
    '''
    sql_peliculas = '''
        CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            idClasificacion_p INTEGER NOT NULL,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            calificacion INTEGER NOT NULL CHECK (calificacion IN (1, 2, 3, 4, 5)),
            FOREIGN KEY (idClasificacion_p) REFERENCES Clasificacion(idClasificacion),
            FOREIGN KEY (Genero) REFERENCES Genero(ID)
        );
    '''
    try:
        conn.cursor.execute(sql_genero)
        conn.cursor.execute(sql_clasificacion)
        conn.cursor.execute(sql_calificacion)
        conn.cursor.execute(sql_peliculas)
        conn.cerrar_con()
        print("Tablas creadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")



class Peliculas():

 
        def __init__(self, nombre, duracion, genero, clasificacion, calificacion):
            self.nombre = nombre
            self.duracion = duracion
            self.genero = genero
            self.clasificacion = clasificacion
            self.calificacion = calificacion

        def __str__(self):
            return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}, {self.clasificacion}, {self.calificacion}]'

def guardar_peli(pelicula):
    conn = Conneccion()

    sql = f'''
        INSERT INTO Peliculas(Nombre, Duracion, Genero, idClasificacion_p, calificacion)
        VALUES('{pelicula.nombre}', '{pelicula.duracion}', {pelicula.genero}, {pelicula.clasificacion}, {pelicula.calificacion});
    '''

    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar la película: {e}")

def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql = '''
       
            SELECT p.ID, p.Nombre, p.Duracion, g.Nombre AS Genero, c.nombreClasificacion, p.calificacion
            FROM Peliculas p
            INNER JOIN Clasificacion c ON p.idClasificacion_p = c.idClasificacion
            INNER JOIN Genero g ON p.Genero = g.ID;
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
        print(f"Géneros obtenidos: {listar_genero}")  
        conn.cerrar_con()

        return listar_genero
    except Exception as e:
        print(f"Error al listar géneros: {e}")
        return []


def listar_Clasificacion():
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


def listar_calificacion():
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
    
    sql = '''
     UPDATE Peliculas
        SET Nombre = ?, Duracion = ?, Genero = ?, idClasificacion_p = ?, calificacion = ?
        WHERE ID = ?;

    '''
    try:
        conn.cursor.execute(sql, (pelicula.nombre, pelicula.duracion, pelicula.genero, pelicula.clasificacion, pelicula.calificacion, id))
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar la película: {e}")

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

        
def buscar_pelicula_por_nombre(nombre):
    conn = Conneccion()
    Peliculas = []

    sql = sql = " SELECT p.ID, p.Nombre, p.Duracion, g.Nombre AS Genero, c.nombreClasificacion, p.calificacion FROM Peliculas p INNER JOIN Clasificacion c ON p.idClasificacion_p = c.idClasificacion INNER JOIN Genero g ON p.Genero = g.ID WHERE p.Nombre like '%"+nombre+"%'; "
       
  
   
    try:
        conn.cursor.execute(sql)
        clasificaciones = conn.cursor.fetchall()
        conn.cerrar_con()

        return clasificaciones
    except Exception as e:
        print(f"Error al buscar clasificación: {e}")
        return []
    
    



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

    