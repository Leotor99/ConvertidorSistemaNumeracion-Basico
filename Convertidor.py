from tkinter import ttk
from tkinter import *

class Convertidor:

    def __init__(self,window):
        self.wind=window
        self.wind.title('ConvertidorSistemasNumeracion')
        # self.wind.minsize(width=500,height=500)
        self.wind.maxsize(width=500,height=500)
        self.wind.geometry("500x500")
        frameInput =LabelFrame(self.wind)    
        frameInput.grid(row=1,column=1,sticky=W+E,padx=137,pady=10)
        #frameInput.pack(fill=BOTH)
        # frameInput.pack(side=TOP)
        # frameInput.pack(pady=10)
        Label(frameInput,text="Base Origen:",font=("Arial Bold",12),foreground="brown").grid(row=1,column=0,pady=20,padx=20)
        self.unidad_origen=Entry(frameInput,width=10)
        self.unidad_origen.grid(row=1,column=1,pady=20,padx=20,ipady=5)
        Label(frameInput,text="Base Destino:",font=("Bold",12),foreground="brown").grid(row=2,column=0,pady=0,padx=0)
        self.unidad_destino=Entry(frameInput,width=10)
        self.unidad_destino.grid(row=2,column=1,pady=20,padx=20,ipady=5)
        Label(frameInput,text="Numero:",font=("Bold",12),foreground="brown").grid(row=3,column=0,pady=20,padx=20)
        self.numero=Entry(frameInput,width=10)
        self.numero.grid(row=3,column=1,pady=20,padx=20,ipady=5)
        ttk.Button(frameInput,text="Convertir",command=self.convertir).grid(row=4,columnspan=2,sticky=W+E,pady=20,padx=20,ipady=5)
        self.frameOuput=LabelFrame(self.wind)
        self.frameOuput.grid(row=2,column=1,sticky=W+E,padx=137,pady=0)
        self.respuesta = Label(self.frameOuput,text="",font=("Arial bold",12),fg="red")
        self.respuesta.grid(row=2,column=2,pady=20,padx=20)
        self.wind.mainloop()

    def obtener_digitos(self,numero):
        numero = numero
        digito=""
        count =0
        digitos=[]
       
        while(count!=len(numero)):  #Se compara si la posicion del no exceda a la del tamaño de la cadena   
            if(numero[count]=="("):  #Si hay un parentesis de abertura se continua con lo demas
                count=count+1        #Se incrementa en uno al count 
                while(numero[count]!=")"): # Mientras sea diferente del parentesis de cierre continuara con lo sgte
                    digito = digito+numero[count]  #Se agrega cifra del digito 
                    count=count+1    #Se incrementa en uno al count 
                digitos.append(digito) #Se agrega al arreglo
                digito=""               #Se resetea el valor del digito
                    
            #Si no hay parentesis agrega como un digito normal
            else:

                digito = numero[count]  
                digitos.append(digito)
                digito=""

            count = count+1    #OJO se le suma uno porque en el primer if() no se debe considerar el parentesis de cierre
                                #y en el else porque quiero seguir con el siguiente digito

        return digitos

    def convertir_base_a_10(self,numero,base_origen):
        digitos = self.obtener_digitos(numero)  #ver el metodo
        resultado=0
        exponente = len(digitos)-1
        for digito in digitos:
            resultado=resultado+(int(digito)*(int(base_origen))**exponente)
            exponente = exponente-1

        return resultado 

    def invertir_cadena(self,digitos):  
        resultado =""
        for digito in reversed(digitos):
            resultado = resultado+digito

        return resultado

    def Convertir_10_a_cualquier_base(self,numero,base_destino):
        numero = int(numero)
        u_destino = int(base_destino)
        digitos = []
        while((numero // u_destino) > 0):  #En este caso uso la division entera para salir del bucle
            if((numero % u_destino)>=10):    #Comparo si el digito es mayor a 10 
                digitos.append("("+str(numero % u_destino)+")") #Si lo es se le coloca parentesis para diferenciar que es un digito 
            else:
                digitos.append(str(numero % u_destino))  #Si es menor solo se agrega a la cadena

                #Utilizo el metodo str para poder concatenar cadenas

            numero=(numero // u_destino)   #El numero cambia de valor al cociente

            if(numero // u_destino==0):     #Hago esta comparacion porque cuando el resto llegue a 0, de alguna forma tengo que obtener el cociente
                if(numero>=10):                     # Comparo si el digito es mayor a 10 
                    digitos.append("("+str(numero)+")")  #Si lo es se le coloca parentesis para diferenciar que es un digito
                else:
                    digitos.append(str(numero))  #Si es menor solo se agrega a la cadena

        return self.invertir_cadena(digitos)   #wachar el metodo



    def errores(self):
        errores = []
        if len(self.unidad_origen.get())==0:
            errores.append('El campo unidad origen es requerido')

        if len(self.unidad_destino.get())==0:
            errores.append('El campo unidad destino es requerido')

        if len(self.numero.get())==0:
            errores.append('El campo numero es requerido')
        
        return errores

    def numeroValido(self,numero):
        numero = self.obtener_digitos(numero)
        b_origen = int(self.unidad_origen.get())
        valido =True
        for digito in numero:
            if(int(digito)>b_origen):
                valido=False

        return valido


    def convertir(self):
        self.respuesta['text']=''
        if (len(self.errores())==0):
            if(self.numeroValido(self.numero.get())):
                numero_b_10 = self.convertir_base_a_10(self.numero.get(),self.unidad_origen.get())
                if(int(numero_b_10)<int(self.unidad_destino.get())):
                    self.respuesta['fg']='green'
                    self.respuesta['text']='Rpta:{}'.format(numero_b_10)
                else:
                    respuesta = self.Convertir_10_a_cualquier_base(numero_b_10,self.unidad_destino.get())
                    self.respuesta['fg']='green'
                    self.respuesta['text']='Rpta:{}'.format(respuesta)  
            else:
                self.respuesta['text']='*Numero invalido=>\n Un digito es mayor que la base'

        else:
            rspta =''
            
            for error in self.errores():
                rspta+='*'+error+'\n'
                self.respuesta['text']=rspta


if __name__=='__main__':
        window =Tk()
        convertidor = Convertidor(window)
       
