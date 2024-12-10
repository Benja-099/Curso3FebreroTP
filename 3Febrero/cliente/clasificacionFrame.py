import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import listar_clasificaciones,guardar_clasificacion,buscar_clasificacion_por_nombre
from modelo.consultas_dao import Clasificacion

import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import listar_clasificaciones, buscar_clasificacion_por_nombre

class ClasificacionFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.id_clasificacion = None
        self.pack()

        self.label_form()
        self.input_form()
        self.boton_buscar()
        self.bloquear_campos()
        self.mostrar_tabla()

    def label_form(self):
        self.label_id = tk.Label(self, text="ID Clasificación: ")
        self.label_id.config(font=('Arial', 12, 'bold'))
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Nombre Clasificación: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)

    def input_form(self):
        self.id_clasificacion_var = tk.StringVar()
        self.entry_id = tk.Entry(self, textvariable=self.id_clasificacion_var)
        self.entry_id.config(width=50)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.nombre_clasificacion_var = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre_clasificacion_var)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

    def boton_buscar(self):

        self.btn_buscar = tk.Button(self, text='Buscar por nombre', command=self.buscar_por_nombre)
        self.btn_buscar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_buscar.grid(row=2, column=1, padx=10, pady=10)
   

    def buscar_por_nombre(self):
        nombre = self.nombre_clasificacion_var.get()
  
        clasificaciones = buscar_clasificacion_por_nombre(nombre)
       
        
      
        for item in self.tabla.get_children():
            self.tabla.delete(item)
      
       
        for c in clasificaciones:
            print(f"Insertando en tabla: ID={c[0]}, Nombre={c[1]}")
            self.tabla.insert('', 'end', text=c[0], values=(c[1],))

    def bloquear_campos(self):
        self.entry_id.config(state='disabled')
        self.entry_nombre.config(state='normal')
        self.id_clasificacion_var.set('')
        self.nombre_clasificacion_var.set('')
        self.id_clasificacion = None

    def mostrar_tabla(self):
        # Crear la tabla para mostrar las clasificaciones
        self.tabla = ttk.Treeview(self, columns=('Nombre Clasificación',))
        self.tabla.grid(row=3, column=0, columnspan=3, sticky='nse')

        # Agregar un scrollbar a la tabla
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=3, column=3, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Configurar los encabezados de la tabla
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre Clasificación')

        # Llenar la tabla con las clasificaciones existentes
        clasificaciones = listar_clasificaciones()
        for c in clasificaciones:
            self.tabla.insert('', 'end', text=c[0], values=(c[1],))
