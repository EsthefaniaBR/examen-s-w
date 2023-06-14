
from tkinter import *
from tkinter import ttk
from tkinter import *
from Casos import *
import mysql.connector
import re
from tkinter import messagebox as mb

def limitar(entrada, limite):
    def limit(event):
        texto = entrada.get()
        if len(texto) >= limite and event.keysym != 'BackSpace':
            return "break"
    entrada.bind("<Key>",limit)



class Casos(Frame):
    def main():
            global root1

    if __name__ == "__main__":
            main()
        
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


        self.habilitarCajas("normal")  
        self.habilitarBtnOper("normal")
        self.id=-1

    def habilitarCajas(self,estado):
        self.txtExpediente.configure(state=estado)
        self.txtPrecio.configure(state=estado)
    
    def habilitarBtnOper(self,estado):
        self.btnAgregar.configure(state=estado)                
           
        
    def limpiarCajas(self):
        self.txtExpediente.delete(0,END)
        self.txtPrecio.delete(0,END)
    

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)      



        
    def fAgregar(self):
        
        agregarpermitido=True;
        expedinente = self.txtExpediente.get()   
        precio= self.txtPrecio.get()
             
        if agregarpermitido==True:
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "123456789",
            port = 3306,
            database = "despacho"
            )
        
            cursor = conexion.cursor()
            consulta = "INSERT INTO `caso`(`EXPEDIENTE`, `PRECIO`) VALUES (%s, %s)"
            valores = (expedinente,precio)
            cursor.execute(consulta,valores)
            

            conexion.commit()
            cursor.close()
            self.insert_data()
            self.limpiarCajas()        
            self.txtExpediente.focus()
        else:
            mb.showerror("Error", "Validar los datos para que sean agregados correctamente.")
            self.limpiarCajas()    


    def fCancelar(self):
        
        r = mb.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == mb.YES:
            self.limpiarCajas()      

    def create_widgets(self):
        root=Tk()
        root.wm_title("Casos")
        #root.geometry("590x250")
        ancho_ventana = 590                 #tamaño de la ventana
        alto_ventana = 250
        x_ventana = root.winfo_screenwidth()//2-ancho_ventana//2
        y_ventana = root.winfo_screenheight()//2-alto_ventana//2
        posicion = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
        root.geometry(posicion)
        root.resizable(0,0)              #prohibe expandir el tamaño de la ventana


        frame1 = Frame(self)
        frame1.place(x=0,y=0,width=93, height=259)        
        
        self.btnAgregar=Button(frame1, text="Agregar", command=self.fAgregar, bg="purple", fg="white")
        self.btnAgregar.place(x=5,y=50,width=80, height=30 )   
       
        frame2 = Frame(root, bg="#E4D376")
        frame2.place(x=0,y=0,width=250, height=759) 

        lbl1 = Label(frame2,text="Expediente: ", bg="#E4D376", font="Arial 11")
        lbl1.place(x=85,y=5)
        self.txtExpediente=Entry(frame2)
        limitar(self.txtExpediente,20)
        self.txtExpediente.place(x=25,y=29,width=200, height=20)   

        lbl2 = Label(frame2,text="Precio: ", bg="#E4D376", font="Arial 11")
        lbl2.place(x=100,y=55)        
        self.txtPrecio=Entry(frame2)
        limitar(self.txtPrecio,6)
        self.txtPrecio.place(x=25,y=79,width=200, height=20)  

        self.btnAgregar=Button(frame2,text="Agregar",command=self.fAgregar, bg="green", fg="white")
        self.btnAgregar.place(x=55,y=170,width=60, height=30)       
  
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=135,y=170,width=60, height=30)
        
        frame3 = Frame(root,bg="ivory" )
        frame3.place(x=247,y=0,width=820, height=800)  

         # mostrar tabla    
        self.tree = ttk.Treeview(frame3, columns=("Expediente", "Precio"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Expediente", text="Expediente")
        self.tree.heading("Precio", text="Precio")
      
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=180, minwidth=180, anchor=CENTER)
        self.tree.column("#2", width=180, minwidth=180, anchor=CENTER)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.configure(height="250")
      
    def insert_data(self):
        expediente = self.txtExpediente.get()
        precio = self.txtPrecio.get()
     

        if expediente and precio:
            # Insertar los datos en la base de datos o en una lista
            # ...
            
            # Agregar los datos a la tabla
            self.tree.insert("", "end", text="1", values=(expediente, precio))
        else:
            mb.showerror("Error", "Todos los campos son requeridos")

        
  
