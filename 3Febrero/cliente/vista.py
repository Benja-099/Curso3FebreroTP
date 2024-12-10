import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas,crear_tabla, guardar_peli,listar_peli,listar_generos,editar_peli,borrar_peli, listar_Clasificacion
from cliente.clasificacionFrame import ClasificacionFrame


class Frame(tk.Frame):  
    def __init__(self, root = None):    
        super().__init__(root,width=480,height=320)    
        self.root = root
        self.id_peli = None   
        self.pack()    
        #self.config(bg='green')

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.mostrar_tabla()
    

    def label_form(self):    
        self.label_nombre = tk.Label(self, text="Nombre: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Duración: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)    
        self.label_nombre = tk.Label(self, text="Genero: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 2, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Clasificacion: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 3, column=0,padx=10,pady=10)
    
    
    def input_form(self):
        self.nombre = tk.StringVar()    
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)    
        self.entry_nombre.config(width=50)    
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10)    
        
        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)    
        self.entry_duracion.config(width=50)    
        self.entry_duracion.grid(row= 1, column=1,padx=10,pady=10) 
        
        x = listar_generos()
        y = []
        for i in x:
            y.append(i[1])

        self.generos = ['Selecione Uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25)    
        self.entry_genero.bind("<<ComboboxSelected>>")    
        self.entry_genero.grid(row= 3, column=1,padx=10,pady=10)

          
        x = listar_Clasificacion()#--------------este agrgege
        y = []
        for i in x:
            y.append(i[1])

        self.clasificacion = ['Selecione Uno'] + y
        self.entry_clasificacion = ttk.Combobox(self, state="readonly")
        self.entry_clasificacion['values'] = self.clasificacion
        self.entry_clasificacion.current(0)
        self.entry_clasificacion.config(width=25)    
        self.entry_clasificacion.bind("<<ComboboxSelected>>")    
        self.entry_clasificacion.grid(row= 2, column=1,padx=10,pady=10)
    
    
    def botones_principales(self):    
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)    
        self.btn_alta.config(width= 10,font=('Arial', 10,'bold'),fg ='#FFFFFF' ,bg='#009973',cursor='hand2',activebackground='#00cc99',activeforeground='#003729', bd=3, relief="raised", highlightthickness=3, highlightbackground="#004d3a")    
        self.btn_alta.grid(row= 4, column=0,padx=10,pady=10)    
        
        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)    
        self.btn_modi.config(width= 10,font=('Arial', 10,'bold'),fg ='#FFFFFF' ,bg='#3399cc',cursor='hand2',activebackground='#2e8ab8',activeforeground='#18475e', bd=3, relief="raised", highlightthickness=3, highlightbackground="#004d3a")    
        self.btn_modi.grid(row= 4, column=1,padx=10,pady=10)    
        
        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cance.config(width= 10,font=('Arial', 10,'bold'),fg ='#FFFFFF' ,bg='#cc3333',cursor='hand2',activebackground='#a32929',activeforeground='#2f0c0c', bd=3, relief="raised", highlightthickness=3, highlightbackground="#004d3a")    
        self.btn_cance.grid(row= 4, column=2,padx=10,pady=10)
    
    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current()
        )

        if self.id_peli == None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula,int(self.id_peli))

        self.bloquear_campos()
        self.mostrar_tabla()
    
    def habilitar_campos(self):    
        self.entry_nombre.config(state='normal')    
        self.entry_duracion.config(state='normal')    
        self.entry_genero.config(state='normal')
        self.entry_clasificacion.config(state='normal')      

        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):    
        self.entry_nombre.config(state='disabled')    
        self.entry_duracion.config(state='disabled')    
        self.entry_genero.config(state='disabled')
        self.entry_clasificacion.config(state='disabled')     

        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.duracion.set('')
        self.entry_genero.current(0)
        self.entry_clasificacion.current(0)
        self.id_peli = None
    
    def mostrar_tabla(self):

        self.lista_p = listar_peli()
        
        self.lista_p.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Duración','Genero','Clasificacion'))
        self.tabla.grid(row=5,column=0,columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=5,column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')
        self.tabla.heading('#4', text='Clasificacion')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values=(p[1],p[2],p[5]))

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)    
        self.btn_editar.config(width= 10,font=('Arial', 10,'bold'),fg ='#FFFFFF' ,bg='#009973',cursor='hand2',activebackground='#00cc99',activeforeground='#003729', bd=3, relief="raised", highlightthickness=3, highlightbackground="#004d3a")    
        self.btn_editar.grid(row= 6, column=0,padx=10,pady=10)    
        
        self.btn_delete = tk.Button(self, text='delete',command=self.eliminar_regristro)    
        self.btn_delete.config(width= 10,font=('Arial', 10,'bold'),fg ='#FFFFFF' ,bg='#cc3333',cursor='hand2',activebackground='#a32929',activeforeground='#2f0c0c', bd=3, relief="raised", highlightthickness=3, highlightbackground="#004d3a")    
        self.btn_delete.grid(row= 6, column=1,padx=10,pady=10)  
    
    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']

            self.nombre_peli = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli = self.tabla.item(self.tabla.selection())['values'][2]
            self.clasi_peli = self.tabla.item(self.tabla.selection())['values'][3]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli)
            self.duracion.set(self.dura_peli)
            self.entry_genero.current(self.generos.index(self.gene_peli))
            self.entry_clasificacion.current(self.clasificacion.index(self.clasi_peli))
        except:
            pass
    
    def eliminar_regristro(self):
        self.id_peli = self.tabla.item(self.tabla.selection())['text']

        borrar_peli(int(self.id_peli))

        self.mostrar_tabla()


def barrita_menu(root):  
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
   # menu_inicio = tk.Menu(barra, tearoff=0)
    #menu_inicio2 = tk.Menu(barra, tearoff=0)

    # niveles 
    # #principal
    #barra.add_cascade(label='Inicio', menu = menu_inicio) #----------------borreeee----------------------------es el menucitp
    #barra.add_cascade(label='Consultas', menu = menu_inicio)  
    barra.add_cascade(label='Clasificación', command=abrir_clasificacion)  # Nuevo menú para Clasificación
    #barra.add_cascade(label='Acerca de..', menu = menu_inicio)  
    #barra.add_cascade(label='Ayuda', menu= menu_inicio2)  
    
    #submenu 
  #  menu_inicio.add_command(label='Conectar DB', command= crear_tabla)  #-------------esto le pertenece a cadsacosa de los menucuiots
   # menu_inicio.add_command(label='Desconectar DB')  
    #menu_inicio.add_command(label='Salir', command= root.destroy)

    #submenu ayuda
   # menu_inicio2.add_command(label='Contactanos')  
    #menu_inicio2.add_command(label='lalala')  
    #menu_inicio2.add_command(label='ola komo stas')
   
def abrir_clasificacion():
    ventana_clasificacion = tk.Toplevel()
    ventana_clasificacion.title("Clasificación")
    ClasificacionFrame(ventana_clasificacion)





    