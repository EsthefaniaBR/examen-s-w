from tkinter import *
from tkinter import ttk
from tkinter import *
from Lista import *
from tkinter import messagebox
import mysql.connector

def main():
    root = Tk()
    root.wm_title("Citas agendadas")
    app = Lista(root)
    app.mainloop()

if __name__ == "__main__":
    main()

class Lista(Frame):
    
    def __init__(self, master=None):
        super().__init__(master,width=550, height=290)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def buscar(self):
        nombre=entry.get()
        apellido= entry_2.get()
        
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="despacho")
        
        cursor=conexion.cursor()
        comando= "SELECT * FROM `datos_del_cliente` WHERE NOMBRE = %s AND AP_PATERNO = %s "
        valores=(nombre,apellido)
        cursor.execute(comando,valores)
        datos=cursor.fetchall()
        if datos:
            for resultados in datos:
                self.tree.insert(parent='', index='end', iid=0, values=(resultados[1], resultados[2]))
        else:
            messagebox.showerror(title="No result",message="El usuario al que esta intentando acceder no esta registrado")
        
    def fbuscar(self):  
        global entry
        global entry_2
            
        buscador=Tk()
        buscador.config(background="antique white")
        buscador.title("Buscador")
        
        message=Label(buscador,text="Ingrese el nombre de la persona que desea buscar",background="antique white")
        message.pack()
        entry=Entry(buscador)
        entry.pack(pady="20")

        message_2=Label(buscador,text="Ingrese el ap.paterno de la persona que desea buscar",background="antique white")
        message_2.pack()
        entry_2=Entry(buscador)
        entry_2.pack(pady="20")

        button=Button(buscador,text="Buscar",background="light goldenrod",command=self.buscar)
        button.pack()
        
        buscador.mainloop()

    def create_widgets(self):

        frame3 = Frame(self,bg="ivory" )
        frame3.place(x=150,y=30,width=535, height=228)     
        #mostrar tabla    
        self.tree = ttk.Treeview(frame3, columns=("num.citas", "hora", "lugar", "fecha"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("num.citas", text="Num.Citas")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("lugar", text="Lugar")
        self.tree.heading("fecha", text="Fecha")
        
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#2", width=100, minwidth=90, anchor=CENTER)
        self.tree.column("#3", width=100, minwidth=90, anchor=CENTER)
        self.tree.column("#4", width=100, minwidth=90, anchor=CENTER)
        self.tree.grid(row=0, column=0, sticky="nsew")

        #botones
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=50,width=93, height=159)        
        self.btnBuscar=Button(frame1,text="Buscar", command=self.fbuscar, bg="purple", fg="white")
        self.btnBuscar.place(x=5,y=50,width=80,height=30)
