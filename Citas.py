from tkinter import *
from tkinter import ttk
from tkinter import *
from Citas import *
from tkinter import messagebox
import mysql.connector
import re


def limitar(entrada, limite):
    def limit(event):
        texto = entrada.get()
        if len(texto) >= limite and event.keysym != 'BackSpace':
            return "break"
    entrada.bind("<Key>",limit)

class Citas(Frame):
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
        self.txtCitas.configure(state=estado)
        self.txtHora.configure(state=estado)
        self.txtLugar.configure(state=estado)
        self.txtfecha.configure(state=estado)
    
    def habilitarBtnOper(self,estado):
        self.btnAgregar.configure(state=estado)                
           
        
    def limpiarCajas(self):
        self.txtCitas.delete(0,END)
        self.txtHora.delete(0,END)
        self.txtLugar.delete(0,END)
        self.txtfecha.delete(0,END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)      

    def fAgregar(self):
        agregarpermitido=True;

        if re.match("^[0-9][0-9]?$",self.txtCitas.get()):  
            citas = self.txtCitas.get()
        else:
            agregarpermitido=False 
            
        if re.match("^[0-9][0-9]?$",self.txtHora.get()):     
            hora = self.txtHora.get()
        else:
            agregarpermitido=False  

        if re.match("^[a-zA-Z ]+$",self.txtLugar.get()):
            lugar = self.txtLugar.get()
        else:
            agregarpermitido=False  
            
        fecha = self.txtfecha.get()

            
        if agregarpermitido==True:
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "123456789",
            port= 3306,
            database = "despacho"
            )
        
            cursor = conexion.cursor()
            consulta = "INSERT INTO `citas`(`NUMERO_CITAS`, `HORA`, `FECHA`,`LUGAR`) VALUES (%s, %s, %s, %s)"
            valores = (citas,hora,fecha,lugar)
            cursor.execute(consulta,valores)
            conexion.commit()
            cursor.close()
            self.insert_data()
            self.limpiarCajas()        
            self.txtCitas.focus()
        else:
            messagebox.showerror("Error", "Validar los datos para que sean agregados correctamente.")    
    
    def fEliminar(self):
        # Obtener los identificadores de las filas seleccionadas
        seleccion = self.tree.selection()
        # Obtener el primer identificador de la selección (si hay uno)
        if len(seleccion) > 0:
            # Variables 
            item = seleccion[0]
            datos = self.tree.item(seleccion[0])  # obtener los datos de la fila seleccionada
            citas = datos['values'][0]  # obtener el valor de la columna 'Nombre'

            #Borrar datos de la BD
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "123456789",
            port = 3306,
            database = "despacho")
            cursor = conexion.cursor()
            sql = "DELETE FROM `citas` WHERE `NUMERO_CITAS` = %s"
            valores = [citas]
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()      
            self.txtCitas.focus()
            
            # Eliminar la fila correspondiente
            self.tree.delete(item)
            
        else:
            # Si no hay ninguna fila seleccionada, mostrar un mensaje de error
            messagebox.showerror("Error", "Debe seleccionar una fila para eliminar.")    
            self.limpiarCajas() 


    def ffecha(self):
        from fecha import Calendario
        Calendario(200,100) 

    def fCancelar(self):
        
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 


    def create_widgets(self):
        root=Tk()
        root.wm_title("Citas")
        #root.geometry("625x280")
        ancho_ventana = 625                 #tamaño de la ventana
        alto_ventana = 280
        x_ventana = root.winfo_screenwidth()//2-ancho_ventana//2
        y_ventana = root.winfo_screenheight()//2-alto_ventana//2
        posicion = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
        root.geometry(posicion)
        root.resizable(0,0)              #prohibe expandir el tamaño de la ventana

        frame1 = Frame(self, bg="#E4D376")
        frame1.place(x=0,y=0,width=93, height=259)        
        
        self.btnAgregar=Button(frame1, text="Agregar", command=self.fAgregar, bg="purple", fg="white")
        self.btnAgregar.place(x=5,y=50,width=80, height=30 )   
       

        frame2 = Frame(root,bg="#E4D376")
        frame2.place(x=0,y=0,width=250, height=759) 

        lbl1 = Label(frame2,text="Num.Citas: ", font="Arial 11", bg="#E4D376")
        lbl1.place(x=85,y=5)        
        self.txtCitas=Entry(frame2, justify=CENTER)
        limitar(self.txtCitas,3)
        self.txtCitas.place(x=25,y=29,width=200, height=25)   

        lbl2 = Label(frame2,text="Hora: ", font="Arial 11", bg="#E4D376")
        lbl2.place(x=105,y=55)        
        self.txtHora=Entry(frame2, justify=CENTER)
        limitar(self.txtHora,4)
        self.txtHora.place(x=25,y=79,width=200, height=25)  

        lbl3 = Label(frame2,text="Lugar: ", font="Arial 11", bg="#E4D376")
        lbl3.place(x=105,y=155)        
        self.txtLugar=Entry(frame2, justify=CENTER)
        limitar(self.txtLugar,20)
        self.txtLugar.place(x=25,y=179,width=200, height=25) 
               
        lbl4 = Label(frame2,text="Fecha: ", font="Arial 11", bg="#E4D376")
        lbl4.place(x=100,y=105)        
        self.btnfecha=Button(frame2,text="Seleccionar fecha", command=self.ffecha, bg="gray", fg="white")
        self.btnfecha.place(x=30,y=129,width=100, height=25)
        self.txtfecha=Entry(frame2)
        limitar(self.txtfecha,10)
        self.txtfecha.place(x=130,y=129,width=100, height=25) 

        self.btnAgregar=Button(frame2,text="Agregar", command=self.fAgregar, bg="Green", fg="white")
        self.btnAgregar.place(x=15,y=220,width=60, height=30)       

        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="Red", fg="white")
        self.btnCancelar.place(x=95,y=220,width=60, height=30)

        self.btnEliminar=Button(frame2,text="Eliminar", command=self.fEliminar, bg="Red", fg="white")
        self.btnEliminar.place(x=175,y=220,width=60, height=30)

        frame3 = Frame(root,bg="ivory" )
        frame3.place(x=247,y=0,width=820, height=800)  

        #mostrar tabla    
        self.tree = ttk.Treeview(frame3, columns=("Número de citas", "Hora", "Lugar", "Fecha"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Número de citas", text="Número de citas")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Lugar", text="Lugar")
        self.tree.heading("Fecha", text="Fecha")

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=100, minwidth=90, anchor=CENTER)
        self.tree.column("#2", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#3", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#4", width=97, minwidth=97, anchor=CENTER)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.configure(height="280")
        
    def insert_data(self):
        citas = self.txtCitas.get()
        hora = self.txtHora.get()
        lugar = self.txtLugar.get()
        fecha = self.txtfecha.get()
        
        if citas and hora and lugar and fecha :
            # Insertar los datos en la base de datos o en una lista
            # ...
            
            # Agregar los datos a la tabla
            self.tree.insert("", "end", text="1", values=(citas, hora, lugar, fecha))
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")

        
        
        
