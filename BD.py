from tkinter import *
from tkinter import ttk
from tkinter import *
from BD import *

def main():
        global root
        root = Tk()
        root.wm_title("Menu")
        ancho_ventana = 230                 #tamaño de la ventana
        alto_ventana = 230
        x_ventana = root.winfo_screenwidth()//2-ancho_ventana//2
        y_ventana = root.winfo_screenheight()//2-alto_ventana//2
        posicion = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
        root.geometry(posicion)
        root.resizable(0,0)         #prohibe expandir el tamaño de la ventana
        app = Ventana(root)
        app.mainloop()

if __name__ == "__main__":
        main()

class Ventana(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, height=230, width=230)
        self.content = Frame(self)  
        self.pack()
        self.create_widgets()
        
    def fClientes(self):
        from clientes import Clientes
        Clientes()
 
    def fCitas(self):  
        from Citas import Citas
        Citas()      
    
    def fCasos(self):
        from Casos import Casos
        Casos()

    def create_widgets(self):
        global frame1
        frame1 = Frame(self, bg="#E4D376")
        frame1.place(x=0,y=0,width=293, height=259)        
        self.btnClientes=Button(frame1,text="Registrar Clientes", command=self.fClientes, bg="#DD005F", fg="white")
        self.btnClientes.place(x=10,y=50,width=100, height=30 )        
        self.btnCitas=Button(frame1,text="Agendar Citas", command=self.fCitas, bg="#DD005F", fg="white")
        self.btnCitas.place(x=120,y=50,width=100, height=30)                
        self.btnCasos=Button(frame1,text="Registrar Casos", command=self.fCasos, bg="#DD005F", fg="white")
        self.btnCasos.place(x=10,y=100,width=100, height=30)    
        self.btnCasos=Button(frame1,text="Citas Agendadas", command=self.fCasos, bg="#DD005F", fg="white")
        self.btnCasos.place(x=120,y=100,width=100, height=30)        
       
       

        
