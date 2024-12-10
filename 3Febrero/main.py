import tkinter as tk
from cliente.vista import Frame,barrita_menu

import os
print("Directorio de ejecución:", os.getcwd())


def main(): 
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    ventana.iconbitmap('img/pochoclos.ico')
    ventana.resizable(0,0)#---------argegreg

    #ventana.resizable(False,False) DORMII ESTO PAV VER QEUD A
         
    barrita_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()
    
if __name__ == '__main__':
    main()
