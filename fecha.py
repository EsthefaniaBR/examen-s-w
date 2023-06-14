from tkinter import *
import calendar
from datetime import datetime
class Calendario:
    lista_fecha=[]
    def __init__(self,x,y):
        self.lista_dias_mes=[]
        self.tupla_meses=("ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic")
        self.tupla_dia=("lun","mar","mie","jue","vie","sab","dom") 
        self.fecha=datetime.now()
        self.calendario=calendar.Calendar()
        self.raiz=Tk()
        self.raiz.geometry("%dx%d+%d+%d"%(240,240,x,y))
        self.raiz.overrideredirect(True)
        self.crear_widgets()
        self.actualizar()
        self.raiz.mainloop()
    
    def crear_widgets(self):
        self.marco_titulo=Frame(self.raiz)
        self.marco_titulo.grid(row=0,column=0)
        self.marco_sem=Frame(self.raiz)
        self.marco_sem.grid(row=1,column=0,pady=2)
        self.marco_mes=Frame(self.raiz)
        self.marco_mes.grid(row=2,column=0)
        self.marco_sel=Frame(self.raiz,height=3)
        self.marco_sel.grid(row=3,column=0)
        self.btn_dec_mes = Button(self.marco_titulo, text="<", width=2, relief="flat",command=self.fun_dec_mes)
        self.btn_dec_mes.grid(row=0, column=0)
        self.lab_mes=Label(self.marco_titulo,text="",width=4)
        self.lab_mes.grid(row=0,column=1,pady=2) 
        self.btn_inc_mes = Button(self.marco_titulo, text=">", width=2, relief="flat",command=self.fun_inc_mes)
        self.btn_inc_mes.grid(row=0,column=2) 
        self.lab_titulo=Label(self.marco_titulo,text="CALENDARIO",width=10) 
        self.lab_titulo.grid(row=0,column=3) 
        self.btn_dec_año = Button(self.marco_titulo, text="<", width=2, relief="flat",command=self.fun_dec_año)
        self.btn_dec_año.grid(row=0,column=4) 
        self.lab_año = Label(self.marco_titulo,text="", width=4)
        self.lab_año.grid(row=0,column=5)
        self.btn_inc_año = Button(self.marco_titulo, text=">", width=2, relief="flat",command=self.fun_inc_año)
        self.btn_inc_año.grid(row=0,column=6)
        # Crea barra dias de la semana
        self.lista_dias_sem=[] 
        for i in range(7):
            self.lista_dias_sem.append(Label(self.marco_sem,text=self.tupla_dia[i],width=4,bg="#AAAAAA")) 
            self.lista_dias_sem[i].grid(row=0,column=i)
            if i==6:
                self.lista_dias_sem[i]["fg"]="#FF0000"
        self.lab_sel_fecha = Label(self.marco_sel, text="Fecha:", width=8)
        self.lab_sel_fecha.grid(row=0,column=0)
        self.fecha_seleccionada=Label(self.marco_sel,text="",width=16) 
        self.fecha_seleccionada.grid(row=0,column=1)
        self.btn_aceptar=Button(self.marco_sel,text="Aceptar",width=6,relief="flat",command=self.fun_aceptar) 
        self.btn_aceptar.grid(row=0,column=2)
        indice=0
        for semana in range(6):
            for dia in range(7):
                self.lista_dias_mes.append(Button(self.marco_mes,text=str(indice),width=3,relief="flat"))
                self.lista_dias_mes[indice].grid(row=semana, column=dia)
                if dia==6:
                    self.lista_dias_mes[indice]["fg"]="#FF0000"
                indice+=1 
        self.lista_dias_mes[0].config(command=lambda: self.fun_sel_dia(0))
        self.lista_dias_mes[1].config(command=lambda: self.fun_sel_dia(1))
        self.lista_dias_mes[2].config(command=lambda: self.fun_sel_dia(2))
        self.lista_dias_mes[3].config(command=lambda: self.fun_sel_dia(3))
        self.lista_dias_mes[4].config(command=lambda: self.fun_sel_dia(4))
        self.lista_dias_mes[5].config(command=lambda: self.fun_sel_dia(5))
        self.lista_dias_mes[6].config(command=lambda: self.fun_sel_dia(6))
        self.lista_dias_mes[7].config(command=lambda: self.fun_sel_dia(7))
        self.lista_dias_mes[8].config(command=lambda: self.fun_sel_dia(8))
        self.lista_dias_mes[9].config(command=lambda: self.fun_sel_dia(9))
        self.lista_dias_mes[10].config(command=lambda: self.fun_sel_dia(10))
        self.lista_dias_mes[11].config(command=lambda: self.fun_sel_dia(11))
        self.lista_dias_mes[12].config(command=lambda: self.fun_sel_dia(12))
        self.lista_dias_mes[13].config(command=lambda: self.fun_sel_dia(13))
        self.lista_dias_mes[14].config(command=lambda: self.fun_sel_dia(14))
        self.lista_dias_mes[15].config(command=lambda: self.fun_sel_dia(15))
        self.lista_dias_mes[16].config(command=lambda: self.fun_sel_dia(16))
        self.lista_dias_mes[17].config(command=lambda: self.fun_sel_dia(17))
        self.lista_dias_mes[18].config(command=lambda: self.fun_sel_dia(18))
        self.lista_dias_mes[19].config(command=lambda: self.fun_sel_dia(19))
        self.lista_dias_mes[20].config(command=lambda: self.fun_sel_dia(20))
        self.lista_dias_mes[21].config(command=lambda: self.fun_sel_dia(21))
        self.lista_dias_mes[22].config(command=lambda: self.fun_sel_dia(22))
        self.lista_dias_mes[23].config(command=lambda: self.fun_sel_dia(23))
        self.lista_dias_mes[24].config(command=lambda: self.fun_sel_dia(24))
        self.lista_dias_mes[25].config(command=lambda: self.fun_sel_dia(25))
        self.lista_dias_mes[26].config(command=lambda: self.fun_sel_dia(26))
        self.lista_dias_mes[27].config(command=lambda: self.fun_sel_dia(27))
        self.lista_dias_mes[28].config(command=lambda: self.fun_sel_dia(28))
        self.lista_dias_mes[29].config(command=lambda: self.fun_sel_dia(29))
        self.lista_dias_mes[30].config(command=lambda: self.fun_sel_dia(10))
        self.lista_dias_mes[31].config(command=lambda: self.fun_sel_dia(31))
        self.lista_dias_mes[32].config(command=lambda: self.fun_sel_dia(32))
        self.lista_dias_mes[33].config(command=lambda: self.fun_sel_dia(33))
        self.lista_dias_mes[34].config(command=lambda: self.fun_sel_dia(34))
        self.lista_dias_mes[35].config(command=lambda: self.fun_sel_dia(35))
        self.lista_dias_mes[36].config(command=lambda: self.fun_sel_dia(36))
        self.lista_dias_mes[37].config(command=lambda: self.fun_sel_dia(37))
        self.lista_dias_mes[38].config(command=lambda: self.fun_sel_dia(38))
        self.lista_dias_mes[39].config(command=lambda: self.fun_sel_dia(39))
        self.lista_dias_mes[40].config(command=lambda: self.fun_sel_dia(40))
        self.lista_dias_mes[41].config(command=lambda: self.fun_sel_dia(41))
        
    def limpiar(self):
         for indice in range(42):
             self.lista_dias_mes[indice]["text"]=""
             self.lista_dias_mes[indice]["state"]="disabled"
             self.lista_dias_mes[indice]["bg"]="#FFFFFF"
                
    def actualizar(self):        
        self.mes=self.calendario.monthdays2calendar(self.fecha.year,self.fecha.month)
        self.lab_mes["text"]=self.tupla_meses[self.fecha.month-1]
        self.lab_año["text"]=self.fecha.year
        self.fecha_seleccionada["text"]=str(self.fecha.day)+"/"+str(self.fecha.month)+"/"+str(self.fecha.year) 
        self.limpiar()
        indice=0
        for semana in self.mes:
            for dia in semana:
                if dia[0]!=0:
                    self.lista_dias_mes[indice]["text"]=dia[0]
                    self.lista_dias_mes[indice]["state"]="normal"
                    if dia[0]==self.fecha.day:
                        self.lista_dias_mes[indice]["bg"]="#FFFF00"
                indice+=1 
         
    def fun_inc_mes(self):
        if self.fecha.month==12:
           self.fecha=datetime(self.fecha.year+1,1,1) 
        else:
            self.fecha=datetime(self.fecha.year,self.fecha.month+1,1)
        self.actualizar()
       
    def fun_dec_mes(self):
            if self.fecha.month==1:
               self.fecha=datetime(self.fecha.year-1,12,1) 
            else:
              self.fecha=datetime(self.fecha.year,self.fecha.month-1,1)
            self.actualizar()
    
    def fun_inc_año(self):
        self.fecha=datetime(self.fecha.year+1,self.fecha.month,self.fecha.day)
        self.actualizar()
    
    def fun_dec_año(self):
        self.fecha=datetime(self.fecha.year-1,self.fecha.month,self.fecha.day)
        self.actualizar() 
    
    def fun_sel_dia(self,d):
        f=datetime(self.fecha.year,self.fecha.month,1)
        dia=d-f.weekday()+1
        self.fecha=datetime(self.fecha.year,self.fecha.month,dia)
        self.actualizar() 
        
    def fun_aceptar(self):
        Calendario.lista_fecha.append(self.fecha.day)
        Calendario.lista_fecha.append(self.fecha.month)
        Calendario.lista_fecha.append(self.fecha.year) 
        self.raiz.destroy() 

    def obtener_fecha(self):
        Calendario(300,300)
        return Calendario.lista_fecha 
       
def obtener_calendario():
    calendario=Calendario(350,200)
    return Calendario.lista_fecha 
           
def main():
   lista= obtener_calendario()
   str_fecha=str(lista[0])+"/"+str(lista[1])+"/"+str(lista[2])
   print(str_fecha)
   print(Calendario.lista_fecha)
    
    
if __name__=="__main__":
    main()
    