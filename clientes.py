from tkinter import *
from tkinter import ttk
from tkinter import *
from clientes import *
import mysql.connector
import re
from tkinter import messagebox

def limitar(entrada, limite):
    def limit(event):
        texto = entrada.get()
        if len(texto) >= limite and event.keysym != 'BackSpace':
            return "break"
    entrada.bind("<Key>",limit)


class Clientes(Frame):
    def main():
            global root1
            root1 = Tk()
            root1.wm_title("registro")   

            app1 = Clientes(root1)
            app1.mainloop()

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
        self.tree.bind("<Double-Button-1>",self.dobleclick)
    
    def dobleclick(self, event):
        self.claveVieja=str(self.tree.item(self.tree.selection())["values"][0])
        self.txtMovil.delete(0,END)
        self.txtNombre.delete(0,END)
        self.txtPaterno.delete(0,END)
        self.txtMaterno.delete(0,END)
        self.txtCalle.delete(0,END)
        self.txtCal1.delete(0,END)
        self.txtCal2.delete(0,END)
        self.txtColonia.delete(0,END)
        
        self.txtMovil.insert(0,str(self.tree.item(self.tree.selection())["values"][0]))
        self.txtNombre.insert(0,str(self.tree.item(self.tree.selection())["values"][1]))
        self.txtPaterno.insert(0,str(self.tree.item(self.tree.selection())["values"][2]))
        self.txtMaterno.insert(0,str(self.tree.item(self.tree.selection())["values"][3]))
        self.txtCalle.insert(0,str(self.tree.item(self.tree.selection())["values"][4]))
        self.txtCal1.insert(0,str(self.tree.item(self.tree.selection())["values"][5]))
        self.txtCal2.insert(0,str(self.tree.item(self.tree.selection())["values"][6]))
        self.txtColonia.insert(0,str(self.tree.item(self.tree.selection())["values"][7]))
        #precio, stock, seccion = data["values"]


    def habilitarCajas(self,estado):
        self.txtMovil.configure(state=estado)
        self.txtNombre.configure(state=estado)
        self.txtPaterno.configure(state=estado)
        self.txtMaterno.configure(state=estado)
        self.txtCalle.configure(state=estado)
        self.txtCal1.configure(state=estado)
        self.txtCal2.configure(state=estado)
        self.txtColonia.configure(state=estado)

    def habilitarBtnOper(self,estado):
        self.btnAgregar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtMovil.delete(0,END)
        self.txtNombre.delete(0,END)
        self.txtPaterno.delete(0,END)
        self.txtMaterno.delete(0,END)
        self.txtCalle.delete(0,END)
        self.txtCal1.delete(0,END)
        self.txtCal2.delete(0,END)
        self.txtColonia.delete(0,END)

    def limpiaGrid(self):
        for i in self.tree.get_children():
            self.tree.delete(i)      

    def fAgregar(self):
        agregarpermitido=True;

        movil = self.txtMovil.get()
        nombre = self.txtNombre.get()
        paterno = self.txtPaterno.get()
        materno= self.txtMaterno.get()
        calle = self.txtCalle.get() 
        cal1 = self.txtCal1.get()
        cal2 = self.txtCal2.get()
        colonia = self.txtColonia.get()
                            
        if agregarpermitido==True:
           conexion = mysql.connector.connect(
           host= "localhost",
           user = "root",
           password = "123456789",
           port = 3306,
           database = "despacho"
           )
           
           cursor = conexion.cursor()
           consulta = "INSERT INTO `datos_del_cliente`(`NUMERO_MOVIL`, `NOMBRE`, `AP_PATERNO`, `AP_MATERNO`, `CALLE`, `CRUZAMIENTO1`, `CRUZAMIENTO2`, `COLONIA`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
           valores = (movil,nombre,paterno,materno,calle,cal1,cal2,colonia)
           cursor.execute(consulta,valores)
           conexion.commit()
           cursor.close()
           self.insert_data()
           self.limpiarCajas()        
           self.txtMovil.focus()
        else:
            messagebox.showerror("Error", "Validar los datos para que sean agregados correctamente.")           
            self.limpiarCajas() 
    
    
    
    def fModificar(self):
            
            movil = self.txtMovil.get()
            nombre = self.txtNombre.get()
            paterno = self.txtPaterno.get()
            materno= self.txtMaterno.get()
            calle = self.txtCalle.get() 
            cal1 = self.txtCal1.get()
            cal2 = self.txtCal2.get()
            colonia = self.txtColonia.get()
            
            
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "123456789",
            port = 3306,
            database = "despacho")
            cursor = conexion.cursor()
            sql = "UPDATE `datos_del_cliente` SET `NOMBRE`= %s, `AP_PATERNO`= %s, `AP_MATERNO`= %s WHERE `NUMERO_MOVIL`= %s"
            valores = (nombre, paterno, materno, movil)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()    
            self.limpiaGrid()
            self.insert_data()
            self.txtMovil.focus()
            

     
            
            

    def fCancelar(self):        
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar")
        if r == messagebox.YES:
            self.limpiarCajas() 

    def create_widgets(self):       
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)        
        
        self.btnAgregar=Button(frame1, text="Agregar", command=self.fAgregar, bg="purple", fg="white")
        self.btnAgregar.place(x=5,y=50,width=80, height=30 )   

        root=Tk()
        root.wm_title("Clientes")
        ancho_ventana = 975                 #tamaño de la ventana
        alto_ventana = 520
        x_ventana = root.winfo_screenwidth()//2-ancho_ventana//2
        y_ventana = root.winfo_screenheight()//2-alto_ventana//2
        posicion = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
        root.geometry(posicion)
        root.resizable(0,0)         #prohibe expandir el tamaño de la ventana

        frame2 = Frame(root,bg="#E4D376") #silver
        frame2.place(x=0,y=0,width=250, height=759) 

        lbl1 = Label(frame2,text="Numero Movil: ", bg="#E4D376", font="Arial 11")
        lbl1.place(x=75,y=10)        
        self.txtMovil=Entry(frame2, justify=CENTER)
        limitar(self.txtMovil,10)
        self.txtMovil.place(x=25,y=34,width=200, height=25)   

        lbl2 = Label(frame2,text="Nombre: ", bg="#E4D376", font="Arial 11")
        lbl2.place(x=93,y=60)        
        self.txtNombre=Entry(frame2, justify=CENTER)
        limitar(self.txtNombre,20)
        self.txtNombre.place(x=25,y=84,width=200, height=25)  

        lbl3 = Label(frame2,text="Ap.Paterno: ", bg="#E4D376", font="Arial 11")
        lbl3.place(x=80,y=110)        
        self.txtPaterno=Entry(frame2, justify=CENTER)
        limitar(self.txtPaterno,15)
        self.txtPaterno.place(x=25,y=134,width=200, height=25) 
               
        lbl4 = Label(frame2,text="Ap.Materno: ", bg="#E4D376", font="Arial 11")
        lbl4.place(x=80,y=160)        
        self.txtMaterno=Entry(frame2, justify=CENTER)
        limitar(self.txtMaterno,15)
        self.txtMaterno.place(x=25,y=184,width=200, height=25) 

        lbl5 = Label(frame2,text="Calle: ", bg="#E4D376", font="Arial 11")
        lbl5.place(x=100,y=210)        
        self.txtCalle=Entry(frame2, justify=CENTER)
        limitar(self.txtCalle,3)
        self.txtCalle.place(x=25,y=234,width=200, height=25) 

        lbl6 = Label(frame2,text="Cruzamiento 1: ", bg="#E4D376", font="Arial 11")
        lbl6.place(x=73,y=260)        
        self.txtCal1=Entry(frame2, justify=CENTER)
        limitar(self.txtCal1,3)
        self.txtCal1.place(x=25,y=284,width=200, height=25) 

        lbl7 = Label(frame2,text="Cruzamiento 2: ", bg="#E4D376", font="Arial 11")
        lbl7.place(x=73,y=310)        
        self.txtCal2=Entry(frame2, justify=CENTER)
        limitar(self.txtCal2,3)
        self.txtCal2.place(x=25,y=334,width=200, height=25) 

        lbl8 = Label(frame2,text="Colonia: ", bg="#E4D376", font="Arial 11")
        lbl8.place(x=95,y=360)        
        self.txtColonia=Entry(frame2, justify=CENTER)
        limitar(self.txtColonia,10)
        self.txtColonia.place(x=25,y=384,width=200, height=25)   

        self.btnAgregar=Button(frame2,text="Agregar", command=self.fAgregar, bg="green", fg="white")
        self.btnAgregar.place(x=20,y=435,width=60, height=30)     

        self.btnModificar=Button(frame2,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=90,y=435,width=60, height=30)

        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=160,y=435,width=60, height=30)

        frame3 = Frame(root,bg="ivory")
        frame3.place(x=247,y=0,width=820, height=800)     
        # mostrar tabla    
        self.tree = ttk.Treeview(frame3, columns=("numero movil", "nombre", "ap.paterno", "ap.materno", "calle", "cruzamiento 1", "cruzamiento 2", "colonia"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("numero movil", text="Numero Móvil")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("ap.paterno", text="Ap.Paterno")
        self.tree.heading("ap.materno", text="Ap.Materno")
        self.tree.heading("calle", text="Calle")
        self.tree.heading("cruzamiento 1", text="Cruzamiento 1")
        self.tree.heading("cruzamiento 2", text="Cruzamiento 2")
        self.tree.heading("colonia", text="Colonia")

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#2", width=120, minwidth=120, anchor=CENTER)
        self.tree.column("#3", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#4", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#5", width=60, minwidth=60, anchor=CENTER)
        self.tree.column("#6", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#7", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#8", width=96, minwidth=96, anchor=CENTER)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.configure(height=520)
      
    def insert_data(self):
        movil = self.txtMovil.get()
        nombre = self.txtNombre.get()
        paterno = self.txtPaterno.get()
        materno = self.txtMaterno.get()
        calle = self.txtCalle.get()
        cal1 = self.txtCal1.get()
        cal2 = self.txtCal2.get()
        colonia = self.txtColonia.get()

        if movil and nombre and paterno and materno and calle and cal1 and cal2 and colonia:
            # Insertar los datos en la base de datos o en una lista
            # ...
            
            # Agregar los datos a la tabla
            self.tree.insert("", "end", text="1", values=(movil, nombre, paterno, materno, calle, cal1, cal2, colonia))
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")

        
        
        
